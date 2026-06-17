---
title: Capabilities
description: Declares the access to protected user resources that the package requires (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Capabilities]
---

# Capabilities

Declares the access to protected user resources that the package requires.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Capabilities>`**

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Capabilities>

    <!-- Child elements -->
    CapabilityChoice{0,100}
    CustomCapabilityChoice{0,1000}
    DeviceCapability{0,1000}

  </Capabilities>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [DeviceCapability](element-f-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 [Device](element-f-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

If you don't explicitly declare the capabilities required for your app to access user resources, your app can't access that resource. However, even if you declare a capability, your app still won't have access to the user resource if it doesn't exist on the system or there are other security policies in place that limit access to the resource.

## Examples

Here's an example of the [Capabilities](../appxmanifestschema2010-v2/element-capabilities.md) node.

```xml
<Capabilities>
    <Capability Name="internetClient"/>
    <Capability Name="internetClientServer"/>
    <Capability Name="privateNetworkClientServer"/>
    <Capability Name="allJoyn"/>
    <uap:Capability Name="documentsLibrary"/>
    <uap:Capability Name="picturesLibrary"/>
    <uap:Capability Name="videosLibrary"/>
    <uap:Capability Name="musicLibrary"/>
    <uap:Capability Name="enterpriseAuthentication"/>
    <uap:Capability Name="sharedUserCertificates"/>
    <uap:Capability Name="userAccountInformation"/>
    <uap:Capability Name="removableStorage"/>
    <uap:Capability Name="appointments"/>
    <uap:Capability Name="contacts"/>
    <uap:Capability Name="phoneCall"/>
    <uap:Capability Name="blockedChatMessages"/>
    <uap:Capability Name="objects3D"/>
</Capabilities>
```

## See also

[App capability declarations](/windows/uwp/packaging/app-capability-declarations)
