---
ms.assetid: d73f5fee-ea46-486e-a23e-3049fd3dee86
title: com:Class (in SurrogateServer/Class)
description: Defines a SurrogateServer class registration (in SurrogateServer/Class).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Class (in SurrogateServer/Class)

Defines a SurrogateServer class registration.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:SurrogateServer\>](element-com-surrogateserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Class\>**

## Syntax

```xml
<com:Class
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    ThreadingModel = 'A string that can be one of the following values: "Both", "STA", "MTA", "MainSTA", "Neutral".'
    DisplayName = 'An optional string with a value between 1 and 256 characters in length. This string is localizable.'
    EnableOleDefaultHandler = 'An optional boolean value.'
    ProgId = 'An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1)'
    VersionIndependentProgId = 'An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1)'
    AutoConvertTo = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    InsertableObject = 'An optional boolean value.'
    ShortDisplayName = 'An optional string with a value between 1 and 40 characters in length.' >

  <!-- Child elements -->
  ( ImplementedCategories,
  Conversion?,
  DataFormats?,
  MiscStatus?,
  Verbs?,
  DefaultIcon?,
  ToolboxBitmap32? 
  )

</com:Class>
```

## Key

`?`    optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The Id attribute corresponds to the CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **Path** | The full path to the surrogate class DLL. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ThreadingModel** | The threading model for loading DLLs. | A string that can be one of the following values: *Both*, *STA*, *MTA*, *MainSTA*, *Neutral*. | Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **EnableOleDefaultHandler** |This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | An optional boolean value. | No |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1) | No |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An optional alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1) | No |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **InsertableObject** | Indicates that this class is insertable. | An optional boolean value. | No |  |
| **ShortDisplayName** | A short version of the class display name. | An optional string with a value between 1 and 40 characters in length. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [ImplementedCategories](element-com-surrogate-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com-surrogate-conversion.md) | Specifies the read/write permissions of a class. |
| [DataFormats](element-com-surrogate-dataformats.md) | Specifies the default and main data formats supported. |
| [MiscStatus](element-com-surrogate-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com-surrogate-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com-surrogate-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com-surrogate-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:SurrogateServer](element-com-surrogateserver.md)  | Registers a SurrogateServer with one or many class registrations. |

## Remarks

Class registrations with the same AppId should share a **SurrogateServer**, unless they need to be registered under different Applications/Application manifest elements.

The **ThreadingModel** corresponds to the [InprocServer32](/windows/win32/com/inprocserver32) threading model. **SurrogateServer** class registrations should have an InprocServer32 registration in the package's private hive.

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
