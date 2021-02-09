---
description: The package block map file is an XML document that contains a list of the app’s files along with indexes and cryptographic hashes for each block of data that is stored in the package.
Search.Product: eADQiWindows 10XVcnh
title: App package block map
ms.assetid: 8be602d7-b7f7-4797-899a-c0a7852725d2


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# App package block map


## Purpose


The package block map file is an XML document that contains a list of the app’s files along with indexes and cryptographic hashes for each block of data that is stored in the package.

## Developer audience


Visual Studio and the [MakeAppx](/windows/win32/appxpkg/make-appx-package--makeappx-exe-) packaging utility automatically create and insert a package block map (AppxBlockMap.xml) when they build each app ZIP package.

Use the block map file to:

-   Understand the structure and content of a block map file that is required for tools that you want to create to produce app packages
-   Check and re-validate the app content after the app deploys

## In this section


-   [Package block map schema reference](../BlockMapSchema/schema-root.md)

## Related topics


[Packaging apps](/windows/uwp/packaging/)

 

 
