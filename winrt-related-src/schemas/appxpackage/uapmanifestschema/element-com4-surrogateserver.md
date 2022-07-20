---
title: com4:SurrogateServer
description: Registers a SurrogateServer with one or many class registrations. (com4:SurrogateServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:SurrogateServer



## Description
Registers a SurrogateServer with one or many class registrations.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:SurrogateServer&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:SurrogateServer     CustomSurrogateExecutable = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    LaunchAndActivationPermission = [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).
    AppId = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    SystemSurrogate = "PreviewHost"
>
<!-- Child elements -->
  Class
  InProcessServerClassReference
  ClassReference
</com4:SurrogateServer>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| CustomSurrogateExecutable |  A path to the DllSurrogate in the AppId key. This path is relative to the package root and must reference a file in the package. This is mututally exclusive with SystemSurrogate. | One of the following values: A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| DisplayName | DisplayName is a localizable string corresponding to the default AppID key value. | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| LaunchAndActivationPermission | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).| Yes |
| AppId | The AppId that references the associated AppId key.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| SystemSurrogate | A value that corresponds to well-known values from the DllSurrogate value of the AppId key. This is mututally exclusive with CustomSurrogateExecutable. | "PreviewHost"| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-surrogateserver-class.md) | Defines a surrogate server class registration. |
| [InProcessServerClassReference](element-com4-inprocessserverclassreference.md) | Specifies the class with which the managed in-process server is associated and sets registration details. |
| [ClassReference](element-com4-surrogateserver-classreference.md) | Specifies the class with which the registered in-process server is associated and sets registration details. |

## Remarks

The CLSID Key](/windows/win32/com/clsid-key-hklm) in the COM registry layout enables a CLSID to be registered for inproc activation ([CLSCTX_INPROC_SERVER](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)) and for outofproc activation in a surrogate server ([CLSCTX_LOCAL_SERVER](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)) by specifying:

- Inproc activation details in an [InprocServer32](/windows/win32/com/inprocserver32) subkey.
- A reference to an AppID key via the AppID value of the CLSID key, where the AppID key specifies a surrogate via the [DllSurrogate](/windows/win32/com/dllsurrogate) value. Note that for outofproc activation in a surrogate server, the inproc server registration details, e.g. dll path and [ThreadingModel](/windows/win32/com/choosing-the-threading-model), are also used in outofproc activation. The **ClassReference** child of the [InProcessServer](element-com4-inprocessserver.md) element enables a package that registers a CLSID for both inproc and outofproc activation to specify the inproc server details once, as an [InProcessServer/Class](element-com4-inprocessserver-class.md) or **InProcessServer/ClassReference** element, and reference this element from the SurrogateServer that supports outofproc activation of the CLSID. This structure for the inproc/outofproc registrations more closely reflects the COM registry layout than independently specifying the dll path and ThreadingModel in both InProcessServer/ClassReference and SurrogateServer/ClassReference elements.

When packaging an application with a CLSID registered for outofproc activation in a surrogate server, it is generally recommended that only the surrogate server is registered in the manifest. For example, surrogate registrations are often used to support COM-based extension points that historically enabled inproc server implementations but which now recommend an outofproc server registration as a best practice for isolation. For packaged applications, there are additional functional limitations for inproc servers (see [In-ProcessServers](/windows/win32/com/in-process-servers) for details), whereas any package with the [runFullTrust restricted capability](/windows/uwp/packaging/app-capability-declarations) can successfully register a surrogate server, and for most extension points registering a surrogate server is sufficient to enable the functionality of the extension. However, if a packaged application needs to support inproc activation of its CLSIDs for compatibility with other applications that request inproc activation (CLSCTX_INPROC_SERVER), and satisfies the requirements for registering an inproc server, it can register the CLSID for inproc activation and outofproc activation in a surrogate. In this case, it is recommended to provide the inproc server details in an **InProcessServer/Class** or **InProcessServer/ClassReference** element, and reference them from a [SurrogateServer](element-com4-serviceserver.md)/[InProcessServerClassReference](element-com4-inprocessserverclassreference.md) element.

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
