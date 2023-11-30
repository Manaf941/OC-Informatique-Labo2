// exo4 in rust

use rand::Rng;

fn main() -> std::io::Result<()> {
    println!("Throw(s):");

    let mut input = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut input)?;
    let throws: u64 = input.trim().parse().unwrap();

    let start = std::time::Instant::now();

    // spawn threads, amount recommended by the OS
    let threads_count = std::thread::available_parallelism()?.get() as u64;
    let mut threads = Vec::with_capacity(threads_count as usize);
    let chunksize = throws/threads_count/64;
    let thread_load = throws/threads_count;
    // divide work by threads
    for _ in 0..threads_count {
        threads.push(std::thread::spawn(move || {
            let mut tails: u64 = 0;
            // separate throws in 64 bits chunks
            for _ in 0..chunksize {
                let mut res:u64 = rand::thread_rng().gen_range(0..u64::MAX);
                // count each set bit in the chunk
                // taken from https://stackoverflow.com/a/8898977/20318035
                while res != 0 {
                    let b = res & (!res + 1);
                    tails += 1;
                    res ^= b;
                }
            }
            
            // heads is the rest of the throws
            (thread_load - tails, tails)
        }));
    }

    let mut heads: u64 = 0;
    let mut tails: u64 = 0;
    // sum results
    for thread in threads {
        let (h, t) = thread.join().unwrap();
        heads += h;
        tails += t;
    }
    let duration = start.elapsed().as_secs_f32();

    let actual_throws = heads+tails;
    println!("Heads: {} {}%", heads, heads as f64 / actual_throws as f64);
    println!("Tails: {} {}%", tails, tails as f64 / actual_throws as f64);
    println!("Aimed Throws: {}", throws);
    println!("Actual Throws: {}", heads+tails);
    println!("Time: {} seconds", duration);

    Ok(())
}