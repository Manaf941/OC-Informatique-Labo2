// This script should be run with bun (bun exo4.random.mjs)
// https://bun.sh
let throws = 0
console.log("Throws(s): ")
for await(const line of console) {
    throws = parseInt(
        line.trim().replace(/_/g, "")
    )
    break
}

if(isNaN(throws) || throws < 1) {
    console.log("Invalid input")
    process.exit(1)
}

const start = performance.now()
let tails = 0

const maxn = 2**32
const chunkcount = Math.ceil(throws / 32)
for(let i = 0; i < chunkcount; i++) {
    // Math.random() should have at least 2**32 precision
    // it depends on the runtime, but we should be safe on bun
    let random = Math.random() * maxn

    // taken from https://stackoverflow.com/a/8898977/20318035
    // we look at the number's bits, each bit set to 1 is a tail, 0 is a head
    while(random) {
        let b = random & (~random + 1)
        tails++
        random ^= b
    }
}
const realthrows = chunkcount*32
const heads = realthrows - tails
const duration = (performance.now() - start) / 1000

function get_percent(val){
    return (val / realthrows * 100).toFixed(6) + "%"
}

console.log(`Heads: ${heads} ${get_percent(heads)}`)
console.log(`Tails: ${tails} ${get_percent(tails)}`)
console.log(`Actual Throws: ${realthrows}`)
console.log(`Aimed Throws: ${throws}`)
console.log(`Time: ${duration} seconds`)

process.exit(0)