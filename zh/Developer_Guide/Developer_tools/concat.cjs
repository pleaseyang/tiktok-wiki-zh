const fs = require('fs');
const base = 'D:/tiktok/tiktok-docs/zh/Developer_Guide/Developer_tools/';
const main = base + 'Seller_Center_development_shops.md';
const parts = ['part2.md','part3.md','part4.md','part5.md','part6.md','part7.md','part8.md'];
let content = fs.readFileSync(main, 'utf-8');
for (const p of parts) {
  const part = fs.readFileSync(base + p, 'utf-8');
  content += '\n' + part;
}
fs.writeFileSync(main, content, 'utf-8');
console.log('Final length:', content.length, 'Lines:', content.split('\n').length);
// Clean up temp files
for (const p of parts) {
  fs.unlinkSync(base + p);
}
fs.unlinkSync(base + 'append1.cjs');
fs.unlinkSync(base + 'append2.cjs');
fs.unlinkSync(base + 'append3.cjs');
fs.unlinkSync(base + 'fix1.cjs');
fs.unlinkSync(base + 'final_append.cjs');
fs.unlinkSync(base + 'write_remaining1.cjs');
console.log('Temp files cleaned up');
