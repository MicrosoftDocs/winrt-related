---
Description: To declare each capability required by your app, add a Capability element to the package manifest.
Search.Product: eADQiWindows 10XVcnh
title: How to specify capabilities in a package manifest
ms.assetid: 7ca1d523-bc49-4009-a2ef-238c713cd907
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# How to specify capabilities in a package manifest


**Note**  For Windows 10, see [**uap:Capability**](uapmanifestschema/element-uap-capability.md), [**Capability**](uapmanifestschema/element-capability.md), and [What's different in Windows 10.](uapmanifestschema/what-s-changed-in-windows-10.md)

 

To declare each capability required by your app, add a [**Capability**](appxmanifestschema/element-capability.md) element to the package manifest.

Alternatively, you can package your app using Visual Studio. See [Packaging your app using Visual Studio](https://msdn.microsoft.com/windows/uwp/packaging/index).

## Instructions

### Step 1:

Follow the steps in [How to create a basic package manifest](how-to-create-a-basic-package-manifest.md).

### Step 2:

Determine the capabilities that your app needs. Any capabilities that are required by an API are listed in the documentation and IntelliSense ToolTip for the API. For more info, see [App capability declarations](https://msdn.microsoft.com/windows/uwp/packaging/app-capability-declarations).

### Step 3:

Add one [**Capability**](https://msdn.microsoft.com/library/windows/apps/br211423) element per capability. Here's an example [**Capabilities**](appxmanifestschema/element-capabilities.md) node that declares 3 capabilities.

```XML
<Capabilities>
  <Capability Name="internetClient"/>
  <Capability Name="musicLibrary"/>
  <Capability Name="videosLibrary"/>
</Capabilities>
```

## Related topics


[How to create a package manifest manually](how-to-create-a-package-manifest-manually.md)

[How to specify device capabilities in a package manifest](how-to-specify-device-capabilities-in-a-package-manifest.md)

 

 



