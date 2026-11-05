const fs = require('fs');
const mainFile = 'D:/tiktok/tiktok-docs/zh/Developer_Guide/Developing_for_the_TikTok_Shop_App_Store/Edit_your_App.md';
let content = fs.readFileSync(mainFile, 'utf-8');
content = content.replace(/\n\| 详细描述.*$/, '');
content += '\n| 详细描述 | 更新应用详情页面