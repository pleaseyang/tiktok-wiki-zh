# 常见错误

When integrating with TikTok Shop Products APIs, it’s essential to understand the correct structure and usage of each parameter to ensure smooth API interactions. In this article, we highlight common mistakes developers make when calling the APIs, particularly for complex parameters, and provide guidance on how to avoid them.

# 销售属性
First, it’s important to understand what sales attributes are and their relationship to SKUs.
**销售属性**是特定于 SKU 的变体，如尺寸、颜色和材料，而 **SKU** 代表这些属性的**唯一**组合，创建产品的不同版本。例如，颜色为"红色"、材料为"棉"的毛衣是一个 SKU，而颜色为"蓝色"、材料为"羊毛"的毛衣是另一个 SKU。

本节重点介绍如何通过实际示例避免在上架产品时定义销售属性的常见错误。
> Note: The examples here use the "name" parameters, but the same principles apply when using the "id" parameters as well.

## 单个 SKU 中的重复销售属性
Each SKU can only **define each sales attribute ID/name once**. In practical terms, this means an SKU can’t have two different colors at the same time. 
### 错误用法
Example: A sweater SKU can't be both red and blue at the same time.
```JSON
// 产品
"skus": [
    { // SKU 1
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",    // 重复值
          "value_name": "Red"
        },
        { // 变体 A
          "name": "Color",    // 重复值
          "value_name": "Blue"
        }
      ]
    }
  ]
```

### 正确用法
Example 1: If you're representing different sweater colors, create separate SKUs for each color instead of assigning multiple values to a single attribute within one SKU.
```JSON
// 产品
"skus": [
    { // SKU 1 - 红色毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"
        }
      ]        
    { // 添加 SKU 2 - 蓝色毛衣
      "sales_attributes": [         
        { // 变体 A
          "name": "Color",
          "value_name": "Blue"
        }
      ]
    }
  ]
```


Example 2: If you're representing a sweater with multiple color elements, such as an outer color and an inner color, each should be defined as a separate sales attribute.
```JSON
// 产品
"skus": [
    { // SKU 1 - 外面红色里面蓝色的毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Outer Color",    // 唯一值
          "value_name": "Red"
        },
        { // 变体 B
          "name": "Inner Color",    // 唯一值
          "value_name": "Blue"
        }
      ]
    }
  ]
```


## 跨 SKU 的重复销售属性值
每个 SKU 必须代表**销售属性值 ID/名称的唯一组合。**实际上，这意味着不能有两个具有相同属性和属性值组合的 SKU。例如，可以有两个红色毛衣的 SKU，但它们必须在另一个属性上有所不同，如尺寸或材料。
### 错误用法 - 1 个属性
Example: You can't have two SKUs for red sweaters.
```JSON
// 产品
"skus": [
    { // SKU 1
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"    // 重复值
        }
      ]
    },
    { // SKU 2
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"    // 重复值
        }
      ]
    }    
  ]
```

### 正确用法 - 1 个属性
Example: Set different colors, red and blue, for each sweater SKU.
```JSON
// 产品
"skus": [
    { // SKU 1 - 红色毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"    // 唯一值
        }
      ]
    },
    { // SKU 2 - 蓝色毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Blue"    // 唯一值
        }
      ]
    }    
  ]
```


### 错误用法 - 多个属性
Example: You can't have two SKUs for red cotton sweaters.
```JSON
// 产品
"skus": [
    { // SKU 1
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"    // 重复值
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"    // 重复值
        }   
      ]
    },
    { // SKU 2
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"    // 重复值
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"    // 重复值
        }
      ]
    }    
  ]
```

### 正确用法 - 多个属性
Example 1: Create an SKU for red cotton sweaters, and another for red wool sweaters.
```JSON
// 产品
"skus": [
    { // SKU 1 - 红色棉质毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"    // 唯一值
        }   
      ]
    },
    { // SKU 2 - 红色羊毛毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Wool"    // 唯一值
        }
      ]
    }    
  ]
```


Example 2: Create an SKU for red cotton sweaters, and another for blue cotton sweaters.
```JSON
// 产品
"skus": [
    { // SKU 1 - 红色棉质毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"    // 唯一值
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"
        }   
      ]
    },
    { // SKU 2 - 蓝色棉质毛衣
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Blue"    // 唯一值
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"
        }
      ]
    }    
  ]
```


## 跨 SKU 的销售属性数量不匹配
所有 SKU 必须定义**相同的销售属性 ID/名称集合**。实际上，这意味着如果一个 SKU 由 2 个销售属性定义（如颜色和材料），则同一产品的每个其他 SKU 也必须包含这两个属性。或者，删除多余的属性。
### 错误用法
Example: You can't have one SKU that defines both color and material, while another SKU only defines color and leaves material unspecified.
```JSON
// 产品
"skus": [
    { // SKU 1
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"
        }   
      ]
    },
    { // SKU 2
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Blue"
        }
         // 缺少变体 B      
      ]
    }    
  ]
```

### 正确用法
Example: Define both color and material for all SKUs.
```JSON
// 产品
"skus": [
    { // SKU 1
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Red"
        },
        { // 变体 B
          "name": "Material",
          "value_name": "Cotton"
        }      
      ]
    },
    { // SKU 2
      "sales_attributes": [ 
        { // 变体 A
          "name": "Color",
          "value_name": "Blue"
        },
        { // 添加变体 B
          "name": "Material",
          "value_name": "Wool"
        }    
      ]
    }    
  ]
```


