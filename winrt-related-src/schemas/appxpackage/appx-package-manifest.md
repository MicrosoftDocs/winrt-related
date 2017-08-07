---
Description: The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows app. 
Search.Product: eADQiWindows 10XVcnh
title: App package manifest
ms.assetid: e3b9d324-c3cd-46e4-b160-37a45e1c349b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 08/07/2017
---

# App package manifest


## Purpose


**Note**  For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows app. This info includes package identity, package dependencies, required capabilities, visual elements, and extensibility points. Every app package must include one package manifest.

The package manifest is digitally signed as part of signing the app package. After signing, you can't modify the manifest without invalidating the package signature. After the package has been installed, the package manifest file appears in the directory for the installed package.

## Developer audience

Visual Studio automatically creates a package manifest. You can also create a package manifest using a text editor.

## In this section

-   [Package manifest schema reference](uapmanifestschema/schema-root.md)
-   [How to create a package manifest manually](how-to-create-a-package-manifest-manually.md)
-   [Localizable manifest items](localizable-manifest-items.md)
-   [Previous app package manifest schemas](previous-schemas-root.md)

## Related topics


[Packaging apps](https://msdn.microsoft.com/library/windows/apps/mt270969)

 

 



