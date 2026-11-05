const fs = require('fs');
const path = 'D:/tiktok/tiktok-docs/zh/Developer_Guide/Developer_tools/Seller_Center_development_shops.md';
let content = fs.readFileSync(path, 'utf-8');

// Remove the incomplete last section
content = content.replace(/# 支持的市场和卖家类型[\s\S]*$/, '');

const remaining = `# 支持的市场和卖家类型
Seller Development Shops 适用于跨境和本地店铺。
**注意：** 下表反映 Core Function Account 的支持区域。对于 Full Function Account，支持的本地