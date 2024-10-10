---
title: com4:TypeLib (in com4:Class and com4:Interface)
description: Associates a type library with a class or interface. (in com4:Class and com4:Interface)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:TypeLib (in com4:Class and com4:Interface)

Associates a type library with a class or interface.

## Element hierarchy

[Package](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[Applications](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[Application](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[Extensions](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[com4:Class](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:TypeLib\>**

&nbsp;&nbsp;&nbsp;&nbsp;[Extensions](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[com4:Class](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:TypeLib\>**

## Syntax

```xml
<com4:TypeLib
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    VersionNumber = 'One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a).' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The type library ID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **VersionNumber** | The version of the type library. | One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a). | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Class](element-com4-class.md) | Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. |

## Remarks

In the com4 version of the syntax, the **Id** attribute must reference the **Id** attribute of a [TypeLib](element-com4-typelib.md) element in the manifest. In the previous version of the syntax, the **Id** must reference a **TypeLib** element in the same **comInterface** extension.

If the **VersionNumber** attribute is present, it must reference the **VersionNumber** attribute of a **TypeLib/Version** element under the **TypeLib** element referenced by the **Id** attribute.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
