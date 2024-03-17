let m = new Map();

m.set('하나', '1');
m.set(1, '하나');
m.set(true, 1);
m.set(false, 0);

console.log(m.get('하나'));
console.log(m.get(true));
console.log(m.has(true));
console.log(m.delete('하나'));
console.log(m.has('하나'));
console.log(m);
console.log(m.size);

for (var varible of m) {
  console.log(varible);
}

console.log(m.keys());
console.log(m.values());
console.log(m.entries());

let temp = new Map([[1, 10], [2, 20], [3, 30], [4, 40]]);

console.log(temp);