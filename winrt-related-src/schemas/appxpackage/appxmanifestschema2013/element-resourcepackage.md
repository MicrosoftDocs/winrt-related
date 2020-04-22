---
Description: Indicates whether the package is a resource package.
Search.Product: eADQiWindows 10XVcnh
title: ResourcePackage
ms.assetid: 51cabad7-a2eb-4fa3-ab52-59298555aefb


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ResourcePackage

Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource.

## Element hierarchy

**&lt;ResourcePackage&gt;**

## Syntax

``` syntax
<ResourcePackage>

  boolean

</ResourcePackage>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

If **ResourcePackage** is set to **true**, the manifest performs these semantic checks, which aren't enforced in the schema. A manifest that violates these semantic checks will just fail to validate via the [Packaging APIs](https://msdn.microsoft.com/library/windows/desktop/hh446766).

-   A resource package can't define the [**Dependencies**](https://msdn.microsoft.com/library/windows/apps/dn423264), [**Capabilities**](../appxmanifestschema/element-capabilities.md), [**Applications**](https://msdn.microsoft.com/library/windows/apps/br211417), [**Extensions**](https://msdn.microsoft.com/library/windows/apps/dn423271), and [**Framework**](https://msdn.microsoft.com/library/windows/apps/dn423276) elements.
-   A resource package can't define [**Package\\Identity\\@ProcessorArchitecture**](https://msdn.microsoft.com/library/windows/apps/br211441), so it always defaults to **neutral**.
-   [**Resources\\Resource**](https://msdn.microsoft.com/library/windows/apps/dn423297) elements for a resource package can only define one type of attribute, for example, only **Language** or **Scale**.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 



