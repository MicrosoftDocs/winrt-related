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

If **ResourcePackage** is set to **true**, the manifest performs these semantic checks, which aren't enforced in the schema. A manifest that violates these semantic checks will just fail to validate via the [Packaging APIs](/windows/win32/appxpkg/interfaces).

-   A resource package can't define the [**Dependencies**](../appxmanifestschema2010-v2/element-dependencies.md), [**Capabilities**](../appxmanifestschema/element-capabilities.md), [**Applications**](../appxmanifestschema/element-applications.md), [**Extensions**](../appxmanifestschema2010-v2/element-extensions.md), and [**Framework**](../appxmanifestschema2010-v2/element-framework.md) elements.
-   A resource package can't define [**Package\\Identity\\@ProcessorArchitecture**](../appxmanifestschema/element-identity.md), so it always defaults to **neutral**.
-   [**Resources\\Resource**](../appxmanifestschema2010-v2/element-resource.md) elements for a resource package can only define one type of attribute, for example, only **Language** or **Scale**.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 