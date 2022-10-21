---
description: Declares the access to protected user resources that the package requires (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Capabilities (Windows 10)
ms.assetid: 508b9a46-3dd4-4bce-875b-fb7cadadceb1
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Capabilities (Windows 10)

Declares the access to protected user resources that the package requires.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Capabilities\>**

## Syntax

```xml
<Capabilities>

  <!-- Child elements -->
  Capability{0,100},
  uap:Capability{0,100},
  DeviceCapability{0,100},
  mobile:Capability{0,100},
  rescap:Capability{0,100},
  uap:Capability{0,100},
  uap2:Capability{0,100},
  uap3:Capability{0,100},
  uap4:Capability{0,100},
  uap4:CustomCapability{0,100},
  uap7:Capability{0,100},
  uap11:Capability{0,100}
  
</Capabilities>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Capability](element-capability.md) | Declares a capability required by a package. |
| [DeviceCapability](element-devicecapability.md) | Declares a device capability required by a package. On Windows 10.0.10240.0, can contain up to 100 **[Device]**(element-device.md) elements. On Windows 10.0.10586.0, can contain up to 1000 (for syntax and examples, see Examples). |
| [mobile:Capability](element-mobile-capability-manual.md) | Declares a capability required by a package. (mobile)|
| [rescap:Capability](element-rescap-capability.md) | Declares a restricted capability required by a package.|
| [uap2:Capability](element-uap2-capability.md) | Declares a capability required by a package. (uap2)|
| [uap3:Capability](element-uap3-capability-manual.md) | Declares a capability required by a package. (uap3)|
| [uap4:Capability](element-uap4-capability.md) | Declares a capability required by a package. (uap4)|
| [uap4:CustomCapability](element-uap4-customcapability.md) | Declares a custom capability required by a package. (uap4) |
| [uap11:Capability](element-uap11-capability.md) | Declares a capability required by a package. (uap11)|


### Parent elements

| Parent element | Description |
|-|-|
| Package | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

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
    <mobile:Capability Name="recordedCallsFolder"/>
</Capabilities>
```

## See also

[App capability declarations](/windows/uwp/packaging/app-capability-declarations)



## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
