---
description: Declares a capability required by a package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Capability (Windows 10)
ms.assetid: ee6bf220-f139-4ad9-a7a7-e621c189b907
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Capability (Windows 10)

Declares a capability required by a package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Capabilities\>](element-capabilities.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Capability\>**

## Syntax

```xml
<Capability
    Name = 'A string that can one of the following values: "internetClient", "internetClientServer", "privateNetworkClientServer", "allJoyn", or "codeGeneration".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the capability. | A string that can one of the following values: *internetClient*, *internetClientServer*, *privateNetworkClientServer*, *allJoyn*, or *codeGeneration*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Capabilities](element-capabilities.md) | Declares the access to protected user resources that the package requires. |

## Remarks

The [App capability declarations](/windows/uwp/packaging/app-capability-declarations) topic describes the capability values.

## Examples

Here's an example of a [Capabilities](element-capabilities.md) node.

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

## Requirements

|   |  Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
