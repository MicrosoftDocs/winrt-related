---
title: Package
description: Defines the root element of an app package manifest (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package]
---

# Package

Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.

## Element hierarchy

**`<Package>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
  IgnorableNamespaces = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  Identity
  PhoneIdentity?
  Properties
  Resources?
  Dependencies
  Capabilities?
  Capabilities?
  Extensions?
  Applications?
  ComExtensions?

</Package>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **IgnorableNamespaces** | Declares namespaces used in the manifest that should be ignored. Ignored namespace elements are not validated and should be considered untrusted. Multiple namespaces are specified with a space between each namespace. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [Identity](element-f-identity.md) | Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package. |
| [mp:PhoneIdentity](element-mp-phoneidentity.md) | If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate. |
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |
| [Resources](element-f-resources.md) | Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains. For details and examples, see [Resource](element-f-resource.md). |
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |
| [uap15:Capabilities](element-uap15-capabilities.md) | Declares the access to protected user resources that a package requires. This element can be used by framework packages. |
| [Extensions](element-f-package-extensions.md) | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |
| [Applications](element-f-applications.md) | Represents one or more apps that comprise the package. |
| **ComExtensions** | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-f-package-extensions.md) | <!-- TODO: Add description --> |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Examples

<!-- Author content goes here -->
