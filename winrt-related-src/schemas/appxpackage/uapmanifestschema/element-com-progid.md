---
ms.assetid: be322b98-2ab7-4a7e-9135-3051b3b00a75
title: com:ProgId
description: A programmatic identifier (ProgID) that can be associated with a CLSID (com:ProgId).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:ProgId

A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:ProgId\>**

## Syntax

```xml
<com:ProgId 
    Id = 'An alphanumeric string separated by a period between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    CurrentVersion = 'An alphanumeric string separated by a period between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The ID of the ProgID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | Yes |  |
| **Clsid** | Associates a ProgID with a CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **CurrentVersion** | The version of the ProgID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com:ComServer](element-com-comserver.md) | Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*. |

## Remarks

The **Clsid** attribute must reference the **Id** attribute of an ExeServer class, SurrogateServer class, or TreatAsClass registration within the same [ComServer](element-com-comserver.md) extension.

For more information on the ProgID, see [\<ProgID\> Key](/windows/win32/com/-progid--key).

> [!NOTE]
> Clsid and CurrentVersion are mutually exclusive, but at least one must be provided.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
