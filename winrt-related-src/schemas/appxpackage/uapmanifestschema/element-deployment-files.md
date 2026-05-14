---
title: deployment:Files
description: Contains one or more **File** elements specifying DLL files that provide DEH functionality that ships outside of an OS release.
ms.date: 09/17/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, deployment:Extension, deployment:DeploymentExtensionHandler, deployment:Files]
---

# deployment:Files

Contains one or more **File** elements specifying DLL files that provide DEH functionality that ships outside of an OS release.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<deployment:Extension>`](element-deployment-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<deployment:DeploymentExtensionHandler>`](element-deployment-deploymentextensionhandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<deployment:Files>`**  

## Syntax

```xml
<deployment:Files>

  <!-- Child elements -->
  deployment:Files {0,1000}
</deployment:Files>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None

### Child elements

| Child element | Description |
|-|-|
| [deployment:File](element-deployment-file.md) | Specifies one or more DLL files that provide DEH functionality that ships outside of an OS release. |

### Parent elements

| Parent element | Description |
|-|-|
| [deployment:DeploymentExtensionHandler](element-deployment-deploymentextensionhandler.md) | Allows an app to specify one or more DLL files that provide DEH functionality that ships outside of an OS release. |


## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/deployment/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
