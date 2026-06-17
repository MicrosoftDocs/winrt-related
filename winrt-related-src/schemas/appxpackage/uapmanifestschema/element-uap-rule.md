---
title: uap:Rule
description: Specifies which pages in the web context have access to the system's geolocation devices and access to the clipboard (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:ApplicationContentUriRules, uap:Rule]
---

# uap:Rule

Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:ApplicationContentUriRules>`](element-uap-applicationcontenturirules.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:Rule>`**  

## Syntax

```xml
<uap:Rule
  Type = 'A required string that can have one of the following values: "include", or "exclude".'
  Match = 'A required string between 1 and 2084 characters in length in the form of a valid URI.'
  WindowsRuntimeAccess = 'An optional string that can have one of the following values: "allowForWebOnly", "all", or "none".'
  uap5:ServiceWorker = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | A string that specifies whether the rule is an inclusion or exclusion rule. | A string that can have one of the following values: *include*, *exclude*. | Yes |  |
| **Match** | The IRI to use in the rule. See RFC 3987: Internationalized Resource Identifiers (IRIs) for details. It is unique per application in the package and is case sensitive. For example, values of *Match* can be: `https://www.microsoft.com/`, or `*.pdf`. | A string between 1 and 2084 characters in length in the form of a valid URI. | Yes |  |
| **WindowsRuntimeAccess** | Declares UWP (Windows Runtime) access from remote sites. This attribute gives control to a developer to specify the set of URIs that can access UWP APIs from their website. This attribute is not allowed if *Type* is set to `exclude`. | An optional string that can have one of the following values: *allowForWebOnly*, *all*, *none*. | No |  |
| **uap5:ServiceWorker** | This represents the registration of a service worker from a web page (a Progressive Web App) to run as a UWP app. If true, it will be determined whether a URL the app navigates to has the permission required to register the app as a service worker. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **uap5** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

> [!NOTE]
> The UWP Windows Runtime class you intend to expose to JavaScript code must be decorated with the *AllowForWeb* attribute where it is declared.


If more than one rule is defined, then the order of the rules is important.

To define the **Match** attribute with an IRI for a web resource, you can specify only secure `https:` sites - unsecure "http:" sites aren't allowed. If you specify a `http:` site, you get a schema semantic check validation error.

For any values that have a [scheme](/windows/uwp/launch-resume/launch-maps-app) in Windows 8.1 (version 6.3.0), the manifest only permits secure `https:` scheme. The manifest fails any other scheme. This rule doesn't apply on Windows 8 apps for backward compatibility.

## Examples

<!-- Author content goes here -->
