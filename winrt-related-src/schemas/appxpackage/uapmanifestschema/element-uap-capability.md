---
title: uap:Capability
description: Declares a capability required by a package (Windows 10; uap:Capability).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Capabilities, uap:Capability]
---

# uap:Capability

Declares a capability required by a package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Capabilities>`](element-f-capabilities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:Capability>`**  

## Syntax

```xml
<uap:Capability
  Name = 'A required string that can have one of the following values: "documentsLibrary", "picturesLibrary", "videosLibrary", "musicLibrary", "enterpriseAuthentication", "sharedUserCertificates", "userAccountInformation", "removableStorage", "appointments", "contacts", "phoneCall", "blockedChatMessages", "objects3D", "voipCall", or "chat".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can have one of the following values: *documentsLibrary*, *picturesLibrary*, *videosLibrary*, *musicLibrary*, *enterpriseAuthentication*, *sharedUserCertificates*, *userAccountInformation*, *removableStorage*, *appointments*, *contacts*, *phoneCall*, *blockedChatMessages*, *objects3D*, *voipCall*, *chat*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-f-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

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
- [App capability declarations](/windows/uwp/packaging/app-capability-declarations)
- [Guidelines for app settings](/windows/uwp/design/app-settings/guidelines-for-app-settings)
