---
title: com4:Class
description: Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts.
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class

Specifies properties of a CLSID registered by the package that can be shared by one or more concrete registrations of the CLSID for different class contexts. For example, consider an ExeServer supporting out-of-process activation ([CLSCTX_LOCAL_SERVER](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)) and a corresponding in-process handler ([CLSCTX_INPROC_HANDLER](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)). By itself, the **com4:Class** element does not register a CLSID for activation, but it can be referenced by elements such as an ExeServer [Class](element-com4-exeserver-class.md)/[ClassReference](element-com4-exeserver-classreference.md) or InProcessHandler [Class](element-com4-inprocesshandler-class.md)/[ClassReference](element-com4-inprocesshandler-classreference.md), in which case its attributes replace the attributes that could otherwise be specified directly in an ExeServer/Class or InProcessHandler/Class element. This syntax is optional for CLSIDs that are registered for a single class context, but is required to register the same CLSID for multiple class contexts because manifest validation requires the Id attribute to be unique among all Class, ExeServer/Class, InProcessHandler/Class, etc., elements in the manifest.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Class\>**

## Syntax

```xml
<com4:Class
  ProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
  VersionIndependentProgId = 'An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
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

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ProgId** | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | No |  |
| **VersionIndependentProgId** | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | No |  |
| **AutoConvertTo** | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **InsertableObject** | Indicates that this class is insertable. | A boolean value. | No |  |
| **ShortDisplayName** | A short version of the class display name. | A string with a value between 1 and 40 characters in length. | No |  |
| **Id** | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **DisplayName** | The class display name. | A string with a value between 1 and 256 characters in length. This string is localizable. | No |  |

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
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

The [CLSID Key](/windows/win32/com/clsid-key-hklm) in the COM registry layout supports two categories of registration information for a CLSID:

- Details of activation for a specific class context. For example, a **LocalServer32** subkey for outofproc activation (CLSCTX_LOCAL_SERVER), an [InprocHandler32](/windows/win32/com/inprochandler32) subkey for activation of an inproc handler (CLSCTX_INPROC_HANDLER), or an [InprocServer32](/windows/win32/com/inprocserver32) subkey for inproc activation (CLSCTX_INPROC_SERVER). The same CLSID can have registrations for any combination of these class contexts, and the activation details for each is specified independently in the corresponding subkeys.
- Information about the CLSID that is shared between class contexts. For example, properties of an OLE server used in OLE scenarios, the set of component categories implemented by the CLSID, etc., are provided via other subkeys of the CLSID key, and if activation details are provided for multiple class contexts these properties are semantically associated with the CLSID, not with a specific class context.

The attributes of a top-level **com4:Class** element correspond to the information in a CLSID key that is shared between class contexts. If a package supports activation of a CLSID for a single class context, the use of the top-level **Class** element is optional and these attributes can alternatively be specified directly in the nested **Class** element (e.g. ExeServer/Class) that provides its activation details. However, the COM registry layout does not provide a way to specify these properties independently for different class contexts, and the APIs that query these properties do not enable the caller to specify a class context. To reflect this aspect of the COM class registration model, the manifest syntax only enables these properties to be specified once for a CLSID, enforced by requiring uniqueness of the Id attribute for top-level and nested Class elements. Therefore, to register multiple class contexts for a CLSID in a package manifest:

- Shared properties must be provided as the attributes of a top-level Class element.
- Per-class context activation details must be provided in nested ClassReference elements, e.g. ExeServer [Class](element-com4-exeserver-class.md)/[ClassReference](element-com4-exeserver-classreference.md) and InProcessHandler [Class](element-com4-inprocesshandler-class.md)/[ClassReference](element-com4-inprocesshandler-class.md) for a CLSID that supports outofproc activation and an inproc handler. The Id attribute of the **ClassReference** element references the top-level Class element containing the shared properties.

## Example

```xml
<com4:Extension Category="windows.comServer">
  ...
  <!-- Example of a CLSID that has both aan inproc server and an exe server implementation, using top level Claass and ClassReference -->
  <com4:Class Id="10000000-0000-0000-0000-000000000009" DisplayName="CLSID_FOO3"/>
  <com4:ExeServer Executable="MyServer.exe" DisplayName="My Server">
    <com4:ClassReference Id="10000000-0000-0000-0000-000000000009" />
  </com4:ExeServer>
  <com4:InProcessServer Path="MyServer.dll">
    <com4:ClassReference Id="10000000-0000-0000-0000-000000000009" ThreadingModel="Both"/>
  </com4:InProcessServer>
  ...
</com4:Extension>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
