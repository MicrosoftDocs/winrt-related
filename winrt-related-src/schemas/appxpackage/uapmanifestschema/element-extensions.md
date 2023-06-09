---
description: Defines one or more extensibility points for the package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Extensions (in Package) (Windows 10)
ms.assetid: 837ae066-b590-4f58-b552-2e9d608f0fac
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Extensions (in Package) (Windows 10)

Defines one or more extensibility points for the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Extensions\>**

## Syntax

```xml
<Extensions>

  <!-- Child elements -->
  Extension{1,10000}

</Extensions>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md)

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of a package extensibility point is the ability to specify a dynamic-link library or executable that contains activatable classes that your code uses.

The **Extension** elements that can be included under the **Package/Extensions** element are enforced by the XML schema. Each of these **Extension** elements have a required **Category** attribute that specifies one or more extension points that the extension supports. Some extensions support both application and package extension categories. The following table lists the extension categories supported for application extensions and the associated **Extension** element that supports each category. A category can be supported for multiple extensions as a versioning mechanism.

| Extension category | Extension |
|--------------------|-----------|
| windows.comServer | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension) |
| windows.comInterface | [com:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com-extension) |
| windows.comServer | [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension) |
| windows.comInterface | [com2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com2-extension) |
| windows.comServer | [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.comInterface | [com4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-com4-extension) |
| windows.deploymentExtensionHandler | [deployment:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-deployment-extension) |
| windows.firewallRules | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-package-extension) |
| windows.desktopEventLogging | [desktop2:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop2-package-extension) |
| windows.mutablePackageDirectories | [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-package-extension) |
| windows.customInstall | [desktop6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-package-extension) |
| windows.shadowCopyExcludeFiles | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.errorReporting | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-extension) |
| windows.shadowCopyExcludeFiles | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-package-extension) |
| windows.errorReporting | [desktop7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop7-package-extension) |
| windows.mutablePackageDirectories | [desktop8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop8-extension) |
| windows.userMutablePackageDirectories | [desktop8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop8-extension) |
| windows.eventTracing | [desktop8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop8-extension) |
| windows.activatableClass.inProcessServer | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.activatableClass.outOfProcessServer | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.activatableClass.proxyStub | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.certificates | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.publisherCacheFolders | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.comInterface | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.loaderSearchPathOverride | [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-extension) |
| windows.classicAppCompatKeys | [rescap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap4-extension) |
| windows.primaryInteropAssemblies | [rescap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-rescap4-extension) |
| windows.hostRuntime | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-package-extension) |
| windows.mediaContentDecryptionModule | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-package-extension) |
| windows.installedLocationVirtualization | [uap10:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap10-package-extension) |
| windows.sharedFonts | [uap4:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap4-extension) |
| windows.activatableClass.outOfProcessServer | [uap5:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap5-extension) |
| windows.loaderSearchPathOverride | [uap6:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap6-package-extension) |
| windows.sharedFonts | [uap7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap7-extension) |
| windows.enterpriseDataProtection | [uap7:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap7-extension) |
| windows.dataProtection | [uap8:Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-uap8-package-extension) |


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

## See also

- [App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
