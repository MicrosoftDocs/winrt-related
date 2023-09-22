---
description: Defines the root element of an app package manifest (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Package (Windows 10)
ms.assetid: ea0f5af0-8191-4ce0-9594-c647f800bd53
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Package (Windows 10)

Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.

## Element hierarchy

**\<Package\>**

## Syntax

```xml
<Package
  IgnorableNamespaces = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  Identity
  & mp:PhoneIdentity?
  & Properties
  & Resources
  & Dependencies
  & Capabilities?
  & Extensions?
  & Applications?
  & uap15:Capabilities?
</Package>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **IgnorableNamespaces** | Declares namespaces used in the manifest that should be ignored. Ignored namespace elements are not validated and should be considered untrusted. Multiple namespaces are specified with a space between each namespace. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Applications](element-applications.md) | Represents one or more apps that comprise the package. |
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |
| [Extensions (type: CT_PackageExtensions)](element-extensions.md) | Defines one or more extensibility points for the package. |
| [Identity](element-identity.md) | Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package. |
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |
| [Resources](element-resources.md) | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |
| [mp:PhoneIdentity](element-mp-phoneidentity.md) | If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate. |
| [uap15:Capabilities](element-uap15-capabilities.md) | Declares the access to protected user resources that the package requires.  This element can be used by non-main packages. This element can only be used by framework packages.|

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

### Parent elements

This is the outermost element in a document. It cannot be contained by any other element.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
