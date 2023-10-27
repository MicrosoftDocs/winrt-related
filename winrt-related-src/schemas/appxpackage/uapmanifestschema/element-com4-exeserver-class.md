---
title: com4:Class (in com4:ExeServer)
description: Defines an ExeServer class registration. (in com4:ExeServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in com4:ExeServer)

Defines an ExeServer class registration.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[com4:ExeServer](element-com4-exeserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

## Syntax

```xml
<com4:Class
  EnableOleDefaultHandler = 'A boolean value.'
  ProgId = 'An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  VersionIndependentProgId = 'An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  AutoConvertTo = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  InsertableObject = 'A boolean value.'
  ShortDisplayName = 'A string with a value between 1 and 40 characters in length.'
  Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' >

<!-- Child elements -->
  ImplementedCategories
  Conversion
  DataFormats
  MiscStatus
  Verbs
  DefaultIcon
  ToolboxBitmap32
  TypeLib

</com4:Class>
```

## Attributes

### Attributes and elements

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **EnableOleDefaultHandler** | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is `Ole32.dll`. Otherwise it should be omitted. The default value is false. | A boolean value. | Yes |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **InsertableObject** | Indicates that this class is insertable. | A boolean value. | Yes |  |
| **ShortDisplayName** | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | Yes |  |
| **Id** | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | A string with a value between 1 and 256 characters in length. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [ImplementedCategories](element-com4-implementedcategories.md) | Specifies categories implemented by the class. |
| [Conversion](element-com4-conversion.md) | Specifies the formats an application can read and write. |
| [DataFormats](element-com4-dataformats.md) | Specifies the default and main data formats supported by an application. |
| [MiscStatus](element-com4-miscstatus.md) | Specifies how to create and display an object. |
| [Verbs](element-com4-verbs.md) | Specifies the verbs to be registered for an application. |
| [DefaultIcon](element-com4-defaulticon.md) | Provides default icon information for iconic presentations of objects. |
| [ToolboxBitmap32](element-com4-toolboxbitmap32.md) | Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. |
| [TypeLib](element-com4-class-typelib.md) | A type library for a class or interface. |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:ExeServer](element-com4-exeserver.md) | Registers an ExeServer with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
