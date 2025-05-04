const txt: string = `Peter Piper picked a peck of pickled peppers.  A peck of pickled peppers Peter Piper picked.  If Peter Piper picked a peck of pickled peppers. Where’s the peck of pickled peppers Peter Piper picked?`

const order = 3
let ngrams: { [index: string]: string[] } = {}

for (let i = 0; i <= txt.length - order; i++) {
    let gram = txt.substring(i, i + order)
    if (!ngrams[gram]) ngrams[gram] = []
    ngrams[gram].push(txt.charAt(i + order))
}

console.log(ngrams)
