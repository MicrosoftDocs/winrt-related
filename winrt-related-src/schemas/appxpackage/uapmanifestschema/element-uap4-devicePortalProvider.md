---

ms.assetid: e6c37b57-76f9-403f-90a7-2b8bda57e905
title: uap4:DevicePortalProvider
description: Defines a Device Portal provider for deployment.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:DevicePortalProvider

## Description
Defines a Device Portal provider for deployment.  See [Write a custom plugin for Device Portal](https://docs.microsoft.com/windows/uwp/debug-test-perf/device-portal-plugin) for more details on implementation. 

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap4-extension.md">&lt;uap4:Extension&gt;</a></dt>
<dd><b>&lt;uap4:DevicePortalProvider&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap4:DevicePortalProvider DisplayName = A string between 1 and 256 characters in length. This string is localizable.
                           AppServiceName = A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only.
                           ContentRoute? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                           HandlerRoute? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >            
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | A friendly display name for the device portal provider. | A string between 1 and 256 characters in length. This string is localizable. | Yes |
| AppServiceName | The name of the app service used to launch the device portal provider. | A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | Yes |
| ContentRoute | A route that's used to declare HTTP content (JavaScript, HTML, and CSS), e.g., /foo| A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| HandlerRoute | The API namespace requested by the provider, e.g., /foo/bar. Any successful HTTP requests will be sent to the provider for handling. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  

## Remarks
This extension requires the **devicePortalProvider** restricted capability and either the **privateNetworkClientServer** or **internetClientServer** capability. Note that the ContentRoute and HandlerRoute do not need to be provided together.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/4</p></td>
</tr>
</tbody>
</table>
