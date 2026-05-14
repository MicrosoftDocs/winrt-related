---
title: deployment:DeploymentExtensionHandler
description: Allows an app to specify one or more DLL files that provide DEH functionality that ships outside of an OS release.
ms.date: 09/17/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, deployment:Extension, deployment:DeploymentExtensionHandler]
---

# deployment:DeploymentExtensionHandler

Allows an app to specify one or more DLL files that provide DEH functionality that ships outside of an OS release.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<deployment:Extension>`](element-deployment-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<deployment:DeploymentExtensionHandler>`**  

## Syntax

```xml
<deployment:DeploymentExtensionHandler>

  <!-- Child elements -->
  deployment:Files
</deployment:DeploymentExtensionHandler>
```

## Attributes and elements

### Attributes

None

### Child elements

| Child element | Description |
|-|-|
| [deployment:Files](element-deployment-files.md) | Contains one or more **File** elements specifying undocked DEH dlls. |

### Parent elements

| Parent element | Description |
|-|-|
| [deployment:Extension](element-deployment-extension.md) | Declares an extensibility point for the app that specifies an undocked deployment extension handler (DEH). |




## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/deployment/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
