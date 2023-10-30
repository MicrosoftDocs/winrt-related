---
title: com4:Class (in com4:SurrogateServer)
description: Defines a surrogate server class registration. (in com4:SurrogateServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in SurrogateServer)

Defines a surrogate server class registration.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:SurrogateServer\>](element-com4-surrogateserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

## Syntax

```xml
<com4:Class
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *'.
    ThreadingModel = 'A string with one of the following values: "Both", "STA", "MTA", "MainSTA", or "Neutral".'
    Virtualization = 'A string with one of the following values: "enabled" or "disabled".'
    EnableOleDefaultHandler = 'A boolean value.'
    ProgId = 'An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    VersionIndependentProgId = 'An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    AutoConvertTo = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    InsertableObject = 'A boolean value.'
    ShortDisplayName = 'A string with a value between 1 and 40 characters in length.'
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The path to the surrogate server DLL. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*` | Yes |  |
| **ThreadingModel** | The threading model for loading DLLs. | A string with one of the following values: *Both*, *STA*, *MTA*, *MainSTA*, or *Neutral*. | Yes |  |
| **Virtualization** | Specifies whether virtualization is used when loading the class. | A string with one of the following values: *enabled* or *disabled*. | Yes |  |
| **EnableOleDefaultHandler** | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | 'A boolean value. | Yes |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **InsertableObject** | Indicates that this class is insertable. | 'A boolean value. | Yes |  |
| **ShortDisplayName** | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | Yes |  |
| **Id** | The Id attribute corresponds to the CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | A string with a value between 1 and 256 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:SurrogateServer](element-com4-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
