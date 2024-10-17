---
description: Defines additional metadata about the package including attributes that describe how the package appears to users (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Properties (Windows 10)
ms.assetid: accc712c-c7b9-45e1-ba02-836abacbd9b5
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Properties (Windows 10)

Defines additional metadata about the package including attributes that describe how the package appears to users.

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Properties\>**

## Syntax

```xml
<Properties>

  <!-- Child elements -->
  Framework?
  & DisplayName
  & PublisherDisplayName
  & Description?
  & Logo
  & ResourcePackage?
  & uap:SupportedUsers?
  & uap6:AllowExecution?
  & desktop6:FileSystemWriteVirtualization?
  & desktop6:RegistryWriteVirtualization?
  & virtualization:FileSystemWriteVirtualization?
  & virtualization:RegistryWriteVirtualization?
  & rescap6:ModificationPackage?
  & uap10:AllowExternalContent?
  & uap10:PackageIntegrity?
  & uap13:AutoUpdate?
  & uap15:DependencyTarget?
  & uap17:UpdateWhileInUse?
  & heap:HeapPolicy?
  )

</Properties>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Description](element-description.md) | A friendly description that can be displayed to users. |
| [DisplayName](element-displayname.md) | A friendly name that can be displayed to users. |
| [Framework](element-framework.md) | Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is *false* by default. You should not specify a value for it unless you are creating a framework. |
| [Logo](element-logo.md) | A path to a file that contains an image. |
| [PublisherDisplayName](element-publisherdisplayname.md) | A friendly name for the publisher that can be displayed to users. |
| [ResourcePackage](element-resourcepackage.md) | Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is *false* by default. You should not specify a value for it unless you are creating a resource. |
| [uap:SupportedUsers](element-uap-supportedusers.md) | Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system. |
| [uap6:AllowExecution](element-uap6-allowexecution.md) | A boolean value that specifies whether packages with executable are allowed to execute. By default, this value is true. |
| [desktop6:FileSystemWriteVirtualization](element-desktop6-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for your desktop application. |
| [desktop6:RegistryWriteVirtualization](element-desktop6-registrywritevirtualization.md) | Indicates whether virtualization for the registry is enabled for your desktop application. |
| [virtualization:FileSystemWriteVirtualization](element-virtualization-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for a package. |
| [virtualization:RegistryWriteVirtualization](element-virtualization-registrywritevirtualization.md) | Indicates whether virtualization for the registry for your package. |
| [rescap6:ModificationPackage](element-rescap6-modificationpackage.md) | Declares that the current package is a modification package for an enterprise application. |
| [uap10:AllowExternalContent](element-uap10-allowexternalcontent.md) | Enables your package manifest to reference content outside the package, in a specific location on disk. See [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps). |
| [uap10:PackageIntegrity](element-uap10-packageintegrity.md) | Specifies the level of run time package integrity checks and remediation for the package. |
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. |
| [uap15:DependencyTarget](element-uap15-dependencytarget.md) | Allows a main package manifest to specify whether the package is a valid target for [dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview). |
| [uap17:UpdateWhileInUSe](element-uap17-updatewhileinuse.md) | Specifies whether the OS should close the app for app updates, or if the update should be deferred until until the next time the app is restarted by the user or a system reboot. |
| [heap:HeapPolicy](element-heap-heappolicy.md) | Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap. |

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```xml
<Properties>
  <DisplayName>ApplicationData SDK Sample</DisplayName>
  <PublisherDisplayName>Microsoft Corporation</PublisherDisplayName>
  <Description>The application data sample.</Description>
  <Logo>images\storeLogo-sdk.png</Logo>
</Properties>
```

## See also

- [Upload app packages](/windows/uwp/publish/upload-app-packages)
- [Create your app by reserving a name](/windows/uwp/publish/create-your-app-by-reserving-a-name)

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
