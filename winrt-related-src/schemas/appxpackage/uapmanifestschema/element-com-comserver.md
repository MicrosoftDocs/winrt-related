---
ms.assetid: 62d02a56-5e34-4b0a-93d5-f4fbec23e0bb
title: com:ComServer
description: Declares a package extension point of type windows.comServer (com:ComServer).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:ComServer

Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:ComServer\>**

## Syntax

```xml
<ComServer>

  <!-- Child elements -->
  com:ExeServer{0,1000},
  com:SurrogateServer{0,1000},
  com:ProgId{0,10000},
  com:TreatAsClass{0,10000}

</ComServer>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [ExeServer](element-com-exeserver.md) | Registers an ExeServer with one or many class registrations. |
| [SurrogateServer](element-com-surrogateserver.md) | Registers an SurrogateServer with one or many class registrations. |
| [ProgId](element-com-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. |
| [TreatAsClass](element-com-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:Extension](element-com-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package. |

## Remarks

In multi-application packages, it's important to place the COM server registration under the correct Applications/Application manifest element, because COM server processes will run with the identity of the ancestor Applications/Application element.

COM servers registered in the manifest always get Activate As Package (AAP) behavior, which means the COM server runs with the user session default token with package and application claims added. This is different from the default activation behavior of classically registered COM servers, in which the COM server runs with the client's token. For most applications, this difference will not be noticeable because clients typically run with the user session default token. Other activation behaviors, such as [RunAs]( /windows/win32/com/runas), are not supported.

> [!NOTE]
> Any registrations in **comServer** that depend on another registration (e.g. a **ProgId** references a **Class**) must be in the same **comServer** extension. 

It is possible to have multiple **comServer** extensions under the Applications/Application element, but that is neither necessary nor recommended.

## Examples

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
