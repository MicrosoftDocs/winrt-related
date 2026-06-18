---
title: Extensions (in Package)
description: Describes the Extensions element.
ms.date: 06/16/2026
ms.topic: reference
no-loc: [Package, Extensions, Package, Extensions]
---

# Extensions (in Package)

Defines one or more extensibility points for the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Extensions>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Extensions>

    <!-- Child elements -->
    Extension{0,100000000}
    ExtensionChoice{0,10000}

  </Extensions>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [Extension](element-f-package-extension.md) | Declares an extensibility point for the package. |

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

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of a package extensibility point is the ability to specify a dynamic-link library or executable that contains activatable classes that your code uses.

The **Extension** elements that can be included under the **Package/Extensions** element are enforced by the XML schema. Each of these **Extension** elements have a required **Category** attribute that specifies one or more extension points that the extension supports. Some extensions support both application and package extension categories. The following table lists the extension categories supported for package extensions and the associated **Extension** element that supports each category. A category can be supported for multiple extensions as a versioning mechanism.

| Extension category | Extension |
|--------------------|-----------|
| windows.activatableClass.inProcessServer | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-f-package-extension) |
| windows.activatableClass.outOfProcessServer | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-f-package-extension) |
| windows.activatableClass.proxyStub | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-f-package-extension) |
| windows.certificates | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-f-package-extension) |
| windows.classicAppCompatKeys | [rescap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap4-extension) |
| windows.comInterface | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension), [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension), [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.comServer | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension), [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension), [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.customDesktopEventLog | [desktop10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop10-extension) |
| windows.customInstall | [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-extension) |
| windows.dataProtection | [uap8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap8-extension) |
| windows.dataShortcuts | [desktop10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop10-extension) |
| windows.deploymentExtensionHandler | [deployment:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-deployment-extension) |
| windows.deploymentStateHandler | deployment3:Extension |
| windows.desktopEventLogging | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.enterpriseDataProtection | [uap7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap7-extension) |
| windows.errorReporting | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.eventTracing | [desktop8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop8-extension) |
| windows.firewallRules | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-extension) |
| windows.folder | [desktop10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop10-extension) |
| windows.hostRuntime | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-extension) |
| windows.installedLocationVirtualization | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-extension) |
| windows.loaderSearchPathOverride | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-extension) |
| windows.mediaContentDecryptionModule | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-extension) |
| windows.mutablePackageDirectories | [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-extension), [desktop8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop8-extension) |
| windows.packageExtension | [uap17:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap17-extension) |
| windows.packageExtensionHost | [uap17:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap17-extension) |
| windows.packagingExtension | deployment3:Extension |
| windows.primaryInteropAssemblies | [rescap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap4-extension) |
| windows.publisherCacheFolders | [f:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-f-package-extension) |
| windows.shadowCopyExcludeFiles | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.sharedFonts | [uap7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap7-extension) |
| windows.sipExtension | deployment3:Extension |
| windows.userMutablePackageDirectories | [desktop8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop8-extension) |

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```xml
<Package>
  <Extensions>
    <Extension Category="windows.activatableClass.proxyStub">
      <ProxyStub ClassId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5">
        <Path>Microsoft.Samples.DllServerAuthoring.Proxies.dll</Path>
        <Interface Name="IToaster" InterfaceId="6a112353-4f87-4460-a908-2944e92686f3" />
        <Interface Name="IToast" InterfaceId="699b1394-3ceb-4a14-ae23-efec518b088b" />
        <Interface Name="IAppliance" InterfaceId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5" />
      </ProxyStub>
    </Extension>
    <Extension Category="windows.activatableClass.inProcessServer">
      <InProcessServer>
        <Path>Microsoft.Samples.DllServerAuthoring.dll</Path>
        <ActivatableClass ActivatableClassId="Microsoft.Samples.DllServerAuthoring.Toaster" ThreadingModel="both" />
      </InProcessServer>
    </Extension>
  </Extensions>
</Package>
```
