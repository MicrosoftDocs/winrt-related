---
title: com4:Extension
description: Provides functionality to expose COM registrations to clients outside of the app package (com4:Extension).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension]
---

# com4:Extension

Provides functionality to expose COM registrations to clients outside of the app package. The com4 extension is a new version that is a superset of and replacement for the previous COM schema versions. See the Remarks section for more information.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:Extension>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:Extension>`**

## Syntax

```xml
<com4:Extension
  Category = 'A required string that can have one of the following values: "windows.comServer", or "windows.comInterface".'
  Executable = 'An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  EntryPoint = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  RuntimeType = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  StartPage = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap10:TrustLevel = 'An optional string that can have one of the following values: "appContainer", or "mediumIL".'
  uap10:RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap10:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Id = 'An optional string between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *.'
  uap11:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string that can have one of the following values: "classic", or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine", or "user".' >

  <!-- Child elements -->
  com4:ComServer?
  com4:ComInterface?

</com4:Extension>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of app extensibility point. | A string that must be one of the following values: *windows.comServer*, *windows.comInterface* (in Application); *windows.comServer*, *windows.comInterface* (in Package). | Yes |  |
| **Executable** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **EntryPoint** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **RuntimeType** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **StartPage** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-f-application.md). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. In the current release, this attribute is unsupported for the com4 extension. The value "mediumIL" is always used. | An optional string that can have one of the following values: *appContainer*, *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. In the current release, this attribute is unsupported for the com4 extension. The value "packagedClassicApp" is always used. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, *win32App*. | No |  |
| **uap10:HostId** | This value Specifies the ID of the host runtime for the extension. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different processes. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-f-application.md). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap11:CurrentDirectoryPath** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string that cannot contain these characters: <, >, &#124;, ?, or *. | No |  |
| **uap11:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether this extension's information is registered with Windows in classic ways (e.g. unpackaged apps register types with COM via the registry) or in new more scoped ways. The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *classic*, *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *machine*, *user*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com4:ComServer](element-com4-comserver.md) | Declares a package extension point of type windows.comServer. The comServer extension may include class registrations, including activation details for the servers that implement these classes, and ProgId and TreatAsClass registrations, which provide additional identifiers used to reference these classes at runtime. |
| [com4:ComInterface](element-com4-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extensions (in Package)](element-f-package-extensions.md) | <!-- TODO: Add description --> |
| [Extensions (in Application)](element-f-application-extensions.md) | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **desktop7** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

The com4 extension is essentially a rewrite of the old windows.comServer/windows.comInterface extension syntax. This extension is a superset of the previous com extension functionality, with identical behavior for the inherited syntax. Manifest validation for the new syntax as used in packaging is better aligned with the semantic requirements of the extension.

- In the previous version, each extension was treated as a separate document, allowing non-unique keys and dangling references to be validated.
- In the previous version, duplication of attributes subject to unique/key constraints was only caught by manifest validation if the duplicated attributes appear in the same instance of the extension. Packages that duplicated these attributes would fail to deploy, with limited diagnostic information to identify the problem.
- In the previous version, a keyref whose referent is in a different instance of the extension would be blocked by manifest validation, which is an artificial restriction relative to what the deployment/runtime behavior support.

Applications targeting Windows 11 that can use the new com4 namespace for all of their windows.comServer/windows.comInterface extensions should use it. Mixing the new namespace with the older namespaces is not recommended, for reasons including:

- Deploying the package on versions that support the new namespace will handle extensions from all namespaces, and any unique identifiers duplicated between extensions using different namespace versions will result in a failure. Use of the older namespaces prevents manifest validation from detecting these errors.
- Due to limitations of the older namespace schemas, a keyref in the old syntax cannot refer to a key in the new syntax because these are in different instances of the extension.

Use of the following com4 syntax semantics have capability requirements:

- CompatMode="classic" requires Microsoft.classicAppCompat_8wekyb3d8bbwe
- Scope="machine" requires Microsoft.classicAppCompatElevated_8wekyb3d8bbwe

The following example shows how to register an out-of-process and an in-process server implementation for the same class.

## Examples

```xml
<com4:Class Id="f4ed7720-9b3a-44a4-xxxx-xxxxxxxxxxxx" DisplayName="CLSID_Foo"/> 
<com:ExeServer Executable="MyServer.exe" DisplayName="My server">  
  <com4:ClassReference Id="f4ed7720-9b3a-44a4-xxxx-xxxxxxxxxxxx"/>  
</com:ExeServer> 
<com4:InProcessServer Path="MyServer.dll">  
  <com4:ClassReference Id="f4ed7720-9b3a-44a4-xxxx-xxxxxxxxxxxx"/>  
</com4:InProcessServer> 

```

### New features in the com4 extension

- Support for in-process servers (both unmanaged and managed) and custom in-process handlers (that is, not the OLE default handler). This capability is currently functionally limited and restricted by policy:
  - This is currently intended for use only by packages with external location; it doesn't work for most normal packages due to ACLs on the install location that prevent the package's dlls from being loaded outside the package. For more information on packages with external location, see [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps).
- It is now possible to associate a TypeLib with a class registration.
