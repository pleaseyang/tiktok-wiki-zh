const fs = require('fs');
const f = 'D:/tiktok/tiktok-docs/zh/Developer_Guide/Developing_for_the_TikTok_Shop_App_Store/Edit_your_App.md';
let c = fs.readFileSync(f, 'utf-8');
c = c.replace(/\n\| .*$/, '');
const lines = [];
lines.push('| 精选媒体和图片 | 批准后更新详情页面上的媒体画廊。 |');
lines.push('| 核心优势 | 更新向评估应用的卖家显示的优势摘要。 |');
lines.push('| 详细描述 | 更新应用详情页面