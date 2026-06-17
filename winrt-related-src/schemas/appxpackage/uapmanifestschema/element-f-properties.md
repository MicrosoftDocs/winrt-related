---
title: Properties
description: Defines additional metadata about the package including attributes that describe how the package appears to users (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Properties]
---

# Properties

Defines additional metadata about the package including attributes that describe how the package appears to users.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Properties>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Properties>

    <!-- Child elements -->
    Framework?
    DisplayName
    PublisherDisplayName
    Description?
    Logo
    ResourcePackage?
    SupportedUsers?
    AllowExecution?
    RegistryWriteVirtualization?
    FileSystemWriteVirtualization?
    FileSystemWriteVirtualization?
    RegistryWriteVirtualization?
    ModificationPackage?
    AllowExternalContent?
    PackageIntegrity?
    AutoUpdate?
    DependencyTarget?
    UpdateWhileInUse?
    UpdateWhileInUse?
    HeapPolicy?
    StageWhileInUse?
    TrustedLaunch?
    AccessControlChoice?
    ApplicationDataChoice?

  </Properties>
</Package>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a framework. |  |  |  |
|  | A friendly name that can be displayed to users. |  |  |  |
|  | A friendly name for the publisher that can be displayed to users. |  |  |  |
|  | A friendly description that can be displayed to users. |  |  |  |
|  | A path to a file that contains an image. |  |  |  |
|  | Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource. |  |  |  |
|  | Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system. |  |  |  |
|  | Indicates whether the contents of the package will be allowed to execute. |  |  |  |
|  | Indicates whether virtualization for the registry is enabled for your desktop application. If disabled, other apps can read or write the same registry entries as your application. |  |  |  |
|  | Indicates whether virtualization for the file system is enabled for your desktop application. If disabled, other apps can read or write the same file system entries as your application. |  |  |  |
|  | Specifies a list of directories for which file system virtualization is disabled for a package. Disabling virtualization enables your app to access the global file system (or registry) locations seen by other apps, rather than the virtualized file system (or registry) that is created for your app. Any data written to these unvirtualized locations will persist after your app is uninstalled. |  |  |  |
|  | Specifies a list of keys for which registry virtualization is disabled for a package. Disabling virtualization enables your app to access the global registry (or file system) locations seen by other apps, rather than the virtualized registry (or file system) that is created for your app. Any data written to these unvirtualized locations will persist after your app is uninstalled. |  |  |  |
|  | Declares that the current package is a [modification package](/windows/msix/modification-packages) for an enterprise application. |  |  |  |
|  | Enables your package manifest to reference content outside the package, in a specific location on disk. See [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps). |  |  |  |
|  | Specifies the level of run time package integrity checks and remediation for the package. If enabled, Windows will perform runtime checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package. |  |  |  |
|  | Specifies automatic update configuration for the app. |  |  |  |
|  | Allows a main package manifest to specify whether the package is a valid target for [dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview). |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
|  | Specifies whether the OS should close the app for app updates, or if the update should be deferred until the next time the app is restarted by the user or a system reboot. The OS will still force-close the app for required OS updates and system reboots. |  |  |  |
|  | Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap. |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
|  | Specifies that Trusted Launch is enabled, which restricts the set of processes that can be launched under a package's identity. |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
|  | Description |  |  |  |
|  | - |  |  |  |
|  | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

| Child element | Description |
|-|-|
| [Framework](element-f-framework.md) | Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a framework. |
| [DisplayName](element-f-displayname.md) | A friendly name that can be displayed to users. |
| [PublisherDisplayName](element-f-publisherdisplayname.md) | A friendly name for the publisher that can be displayed to users. |
| [Description](element-f-description.md) | A friendly description that can be displayed to users. |
| [Logo](element-f-logo.md) | A path to a file that contains an image. |
| [ResourcePackage](element-f-resourcepackage.md) | Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource. |
| [uap:SupportedUsers](element-uap-supportedusers.md) | Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system. |
| [uap6:AllowExecution](element-uap6-allowexecution.md) | Indicates whether the contents of the package will be allowed to execute. |
| [desktop6:RegistryWriteVirtualization](element-desktop6-registrywritevirtualization.md) | Indicates whether virtualization for the registry is enabled for your desktop application. If disabled, other apps can read or write the same registry entries as your application. |
| [desktop6:FileSystemWriteVirtualization](element-desktop6-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for your desktop application. If disabled, other apps can read or write the same file system entries as your application. |
| [virtualization:FileSystemWriteVirtualization](element-virtualization-filesystemwritevirtualization.md) | Specifies a list of directories for which file system virtualization is disabled for a package. Disabling virtualization enables your app to access the global file system (or registry) locations seen by other apps, rather than the virtualized file system (or registry) that is created for your app. Any data written to these unvirtualized locations will persist after your app is uninstalled. |
| [virtualization:RegistryWriteVirtualization](element-virtualization-registrywritevirtualization.md) | Specifies a list of keys for which registry virtualization is disabled for a package. Disabling virtualization enables your app to access the global registry (or file system) locations seen by other apps, rather than the virtualized registry (or file system) that is created for your app. Any data written to these unvirtualized locations will persist after your app is uninstalled. |
| [rescap6:ModificationPackage](element-rescap6-modificationpackage.md) | Declares that the current package is a [modification package](/windows/msix/modification-packages) for an enterprise application. |
| [uap10:AllowExternalContent](element-uap10-allowexternalcontent.md) | Enables your package manifest to reference content outside the package, in a specific location on disk. See [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps). |
| [uap10:PackageIntegrity](element-uap10-packageintegrity.md) | Specifies the level of run time package integrity checks and remediation for the package. If enabled, Windows will perform runtime checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package. |
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. |
| [uap15:DependencyTarget](element-uap15-dependencytarget.md) | Allows a main package manifest to specify whether the package is a valid target for [dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview). |
| **uap16:UpdateWhileInUse** | Specifies whether the OS should close the app for app updates, or if the update should be deferred until the next time the app is restarted by the user or a system reboot. |
| [uap17:UpdateWhileInUse](element-uap17-updatewhileinuse.md) | Specifies whether the OS should close the app for app updates, or if the update should be deferred until the next time the app is restarted by the user or a system reboot. The OS will still force-close the app for required OS updates and system reboots. |
| [heap:HeapPolicy](element-heap-heappolicy.md) | Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap. |
| **deployment2:StageWhileInUse** | <!-- TODO: Add description --> |
| [trustedLaunch:TrustedLaunch](element-trustedlaunch-trustedlaunch.md) | Specifies that Trusted Launch is enabled, which restricts the set of processes that can be launched under a package's identity. |

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

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
