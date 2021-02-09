---
description: The bundle manifest file is an XML document that contains a list of app packages and resource packages in the bundle.
Search.Product: eADQiWindows 10XVcnh
title: Bundle manifest
ms.assetid: 42fb6c69-b278-4c67-8677-d19da91f3831


keywords: windows 10, uwp, schema, bundle manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Bundle manifest


## Purpose


The bundle manifest file is an XML document that contains a list of app packages and resource packages in the bundle.

The bundle manifest contains info about the architectures and resources of each package. When you install the bundle on a computer, you can use this info to determine the subset of packages that apply to that computer.

## Developer audience


Visual Studio and the [MakeAppx](/windows/win32/appxpkg/make-appx-package--makeappx-exe-) packaging utility automatically create and insert a bundle manifest schema (BundleManifest.xml) when they build each ZIP bundle.

## In this section


-   [Bundle manifest schema reference](../BundleManifestSchema/schema-root.md)

## Related topics


[Packaging apps](/windows/uwp/packaging/)

 

 
