---
Description: The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows app. 
Search.Product: eADQiWindows 10XVcnh
title: App package manifest
ms.assetid: e3b9d324-c3cd-46e4-b160-37a45e1c349b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# App package manifest


## Purpose


**Note**  For Windows 10, see [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

The package manifest is an XML document that contains the info the system needs to deploy, display, or update a Windows app. This info includes package identity, package dependencies, required capabilities, visual elements, and extensibility points. Every app package must include one package manifest.

The package manifest is digitally signed as part of signing the app package. After signing, you can't modify the manifest without invalidating the package signature. After the package has been installed, the package manifest file appears in the directory for the installed package.

## Developer audience


Visual Studio automatically creates a package manifest. You can also create a package manifest using a text editor.

## In this section


-   [How to create a package manifest manually](how-to-create-a-package-manifest-manually.md)
-   [Localizable manifest items](https://msdn.microsoft.com/library/windows/apps/dn439795)
-   [Package manifest schema reference](https://msdn.microsoft.com/library/windows/apps/br211473)
-   [Package manifest schema with Windows 8.1 minor extensions reference](https://msdn.microsoft.com/library/windows/apps/dn423313)
-   [Package manifest schema with Windows 8.1 feature extensions reference](https://msdn.microsoft.com/library/windows/apps/dn391692)

## Related topics


[Packaging apps](https://msdn.microsoft.com/library/windows/apps/mt270969)

 

 



