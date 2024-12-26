# Rocket.Chat 繁體中文翻譯指南

## 標準術語表

以下是Rocket.Chat中常用術語的標準翻譯：

| 英文術語 | 標準中文翻譯 |
|----------|--------------|
| Livechat | 全渠道服務 |
| Omnichannel | 全渠道服務 |

## 翻譯原則

1. 保持一致性：使用標準術語表中的翻譯
2. 符合繁體中文使用習慣
3. 保持專業性：使用正確的專業術語
4. 確保語意完整：翻譯後的文字應該清晰易懂

## 翻譯流程

1. 使用verify_json.py驗證JSON文件格式
2. 使用translation_verify.html預覽翻譯效果
3. 提交前進行自我審查
4. 創建Pull Request時提供詳細的變更說明

## 測試方法

1. 運行本地Rocket.Chat實例
2. 切換到繁體中文界面
3. 驗證翻譯在實際界面中的顯示效果

## 提交規範

1. 提交信息格式：`fix(i18n): Update Chinese translations`
2. PR描述中包含變更說明和測試信息
