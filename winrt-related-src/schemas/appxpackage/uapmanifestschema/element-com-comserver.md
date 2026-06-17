---
title: com:ComServer
description: Declares a package extension point of type windows.comServer (com:ComServer).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com:Extension, com:ComServer]
---

# com:ComServer

Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:ComServer>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:ComServer>`**  


## Syntax

```xml
<com:ComServer>

  <!-- Child elements -->
  com:ExeServer{0,1000}
  com:SurrogateServer{0,1000}
  com:TreatAsClass{0,10000}
  com:ProgId{0,10000}
  com:ServiceServer{0,1000}
  com:ExeServer{0,1000}
  com:SurrogateServer{0,1000}
  com:TreatAsClass{0,10000}
  com:ProgId{0,10000}

</com:ComServer>
```

### Key

`{}` specific range of occurrences


## Attributes

None.


## Child elements
| Child element | Description |
|-|-|
| [com:ExeServer](element-com-exeserver.md) | Registers an ExeServer with one or many class registrations. |
| [com:SurrogateServer](element-com-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |
| [com:TreatAsClass](element-com-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey. |
| [com:ProgId](element-com-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |
| [com3:ServiceServer](element-com3-serviceserver.md) | Registers a COM server (with one or more class registrations) hosted in a Windows service that is declared with a corresponding [desktop6:Service](element-desktop6-service.md) element. |
| [com3:ExeServer](element-com3-exeserver.md) | Registers an **ExeServer** with one or many class registrations. |
| [com3:SurrogateServer](element-com3-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |
| [com3:TreatAsClass](element-com3-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey. |
| [com3:ProgId](element-com3-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |

## Parent elements

| Parent element | Description |
|-|-|
| [com:Extension](element-com-extension.md) | Provides functionality to expose COM registrations to clients outside of the app package. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

In multi-application packages, it's important to place the COM server registration under the correct Applications/Application manifest element, because COM server processes will run with the identity of the ancestor Applications/Application element.

COM servers registered in the manifest always get Activate As Package (AAP) behavior, which means the COM server runs with the user session default token with package and application claims added. This is different from the default activation behavior of classically registered COM servers, in which the COM server runs with the client's token. For most applications, this difference will not be noticeable because clients typically run with the user session default token. Other activation behaviors, such as [RunAs]( /windows/win32/com/runas), are not supported.

> [!NOTE]
> Any registrations in **comServer** that depend on another registration (e.g. a **ProgId** references a **Class**) must be in the same **comServer** extension.

It is possible to have multiple **comServer** extensions under the Applications/Application element, but that is neither necessary nor recommended.

## Examples

<!-- Author content goes here -->
