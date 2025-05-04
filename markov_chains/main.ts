const txt: string = `Peter Piper picked a peck of pickled peppers.  A peck of pickled peppers Peter Piper picked.  If Peter Piper picked a peck of pickled peppers. Where’s the peck of pickled peppers Peter Piper picked?`

const order: number = 3
let ngrams: { [index: string]: number } = {} 

for (let i = 0; i <= txt.length - order; i++)
{
    // this is because you want to extract i and the three characters succeeding it
    let gram = txt.substring(i, i+order)

    // if it exists it'll return true. if it doesnt, then move to else
    if (ngrams[gram]) { ngrams[gram]++ }
    // when not found then create a new element inside the object with 1st occurance
    else { ngrams[gram] = 1 }
}

console.log(ngrams)
