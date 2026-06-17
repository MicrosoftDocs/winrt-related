---
title: Capability
description: Declares a capability required by a package (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Capabilities, Capability]
---

# Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Capability>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Capability
    Name = 'A required string that can have one of the following values: "internetClient", "internetClientServer", "privateNetworkClientServer", "allJoyn", or "codeGeneration".' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *internetClient*, *internetClientServer*, *privateNetworkClientServer*, *allJoyn*, *codeGeneration*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

The [App capability declarations](/windows/uwp/packaging/app-capability-declarations) topic describes the capability values.

## Examples

Here's an example of a [Capabilities](element-f-capabilities.md) node.

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

[Guidelines for app settings](/windows/uwp/design/app-settings/guidelines-for-app-settings)
