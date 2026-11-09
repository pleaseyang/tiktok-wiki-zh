# 常见错误

与 TikTok Shop Products APIs 集成时，务必理解每个参数的正确结构与用法，以确保接口交互顺畅。本文重点介绍开发者调用接口时（尤其是复杂参数）常犯的错误，并提供规避指导。

# 销售属性
首先，务必理解什么是销售属性，以及它们与 SKU 的关系。
**销售属性**是特定于 SKU 的变体，如尺寸、颜色和材料，而 **SKU** 代表这些属性的**唯一**组合，创建商品的不同版本。例如，颜色为"红色"、材料为"棉"的毛衣是一个 SKU，而颜色为"蓝色"、材料为"羊毛"的毛衣是另一个 SKU。

本节重点介绍如何通过实际示例避免在上架商品时定义销售属性的常见错误。
> 注意: 此处的示例使用 "name" 参数，但使用 "id" 参数时同样适用这些原则。

## 单个 SKU 中的重复销售属性
每个 SKU 只能**为每个销售属性 ID/名称各定义一次**。实际上，这意味着一个 SKU 不能同时拥有两种不同的颜色。
### 错误用法
示例：一个毛衣 SKU 不能同时是红色和蓝色。
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
示例 1: 如果要表示毛衣的不同颜色，请为每种颜色分别创建 SKU，而不是在单个 SKU 内为一个属性指定多个值。
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


示例 2: 如果要表示一件含多种颜色元素的毛衣（例如外色和内色），每种颜色都应定义为单独的销售属性。
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
示例：红色毛衣不能有两个 SKU。
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
示例: 为每件毛衣 SKU 设置不同的颜色，如红色和蓝色。
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
示例：红色棉质毛衣不能有两个 SKU。
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
示例 1: 为红色棉质毛衣创建一个 SKU，为红色羊毛毛衣创建另一个。
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


示例 2: 为红色棉质毛衣创建一个 SKU，为蓝色棉质毛衣创建另一个。
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
所有 SKU 必须定义**相同的销售属性 ID/名称集合**。实际上，这意味着如果一个 SKU 由 2 个销售属性定义（如颜色和材料），则同一商品的每个其他 SKU 也必须包含这两个属性。或者，删除多余的属性。
### 错误用法
示例: 不能让一个 SKU 同时定义颜色和材质，而另一个 SKU 只定义颜色却不指定材质。
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
示例：为所有 SKU 同时定义颜色和材质。
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


