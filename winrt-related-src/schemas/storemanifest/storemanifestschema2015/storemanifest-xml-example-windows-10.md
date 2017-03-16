---
title: StoreManifest XML example (Windows 10)
description: Here's an example of a StoreManifest XML file for a UWP package.
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 7B824C5B-86F8-4310-9B0D-E88BF2BF95BF
author: laurenhughes
ms.author: lahugh
windows 10, uwp, schema, storemanifest
---

# StoreManifest XML example (Windows 10)


Here's an example of a StoreManifest XML file for a UWP package.

This XML declares the app as a Windows Store device app that is tied to a single device experience. It also declares the minimum memory and DirectX level necessary to install the app on a device.

```XML
<?xml version="1.0" encoding="utf-8"?>
<StoreManifest xmlns="http://schemas.microsoft.com/appx/2015/StoreManifest">
  <DeviceCompanionApplication>
    <ExperienceId>258E1783-155C-4577-9077-DBF6A4B71A01</ExperienceId>
  </DeviceCompanionApplication>
  <Dependencies>
    <MemoryDependency MinForeground="750MB" />
    <DirectXDependency Name="D3D12_HWFL_11_0" />
  </Dependencies>
</StoreManifest>
```

 

 




