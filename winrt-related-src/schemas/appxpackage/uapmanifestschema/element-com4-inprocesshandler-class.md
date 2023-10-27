---
title: com4:Class (in InProcessHandler)
description:  Defines an in-process handler class registration. (in com4:InProcessHandler)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in InProcessHandler)

Defines an in-process handler class registration.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessHandler\>](element-com4-inprocesshandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

## Syntax

```xml
<com4:Class
    Virtualization = 'A string that can have one of the following values: "enabled" or "disabled".'
    ProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    VersionIndependentProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    AutoConvertTo = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    InsertableObject = 'A boolean value.'
    ShortDisplayName = 'A string with a value between 1 and 40 characters in length.'
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
| -----------| -------------| -----------| ----------|-|
| **Virtualization** | Specifies whether virtualization is used when loading the class.  | A string that can have one of the following values: *enabled* or *disabled*. | Yes |  |
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **InsertableObject** | Indicates that this class is insertable. | A boolean value. | Yes |  |
| **ShortDisplayName** | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | Yes |  |
| **Id** | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the CLSID's key. | A string with a value between 1 and 256 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:InProcessHandler](element-com4-inprocesshandler.md) | Registers an in-process handler with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| Minimum OS Version | Windows 10 (Build 20348) |
