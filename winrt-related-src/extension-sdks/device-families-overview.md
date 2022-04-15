---
title: Programming with extension SDKs
description: An explanation of device families, extension SDKs, and API contracts, and how to program with them.
ms.topic: reference
ms.date: 09/02/2020
keywords: windows 10, uwp, device family, extension sdk, api contract
---

# Programming with extension SDKs

In order to understand how Windows 10 allows your Universal Windows Platform (UWP) app to most effectively target different classes of devices, this topic explains the following concepts.

- Device family
- Extension SDK
- API contract

We also show how to use them in your programming.

## Video&mdash;Introduction to UWP and device families
&nbsp;
<iframe src="https://www.youtube.com/embed/f20saEKeSpE" width="640" height="360" allowFullScreen frameBorder="0"></iframe>

## Device families, and your app's target device family

A device family identifies the APIs, system characteristics, and behaviors that you can expect across a class of devices.

![device families](images/device-family-tree.png)

A device family is the foundation of an operating system (OS). For example, PCs and tablets run a desktop edition of the OS, and that's based on the Desktop device family. IoT devices run an IoT edition of the OS, which is based on the IoT device family.

Each child device family adds its own APIs to the APIs that it inherits from the Universal device family. The resulting union of APIs in a child device family is guaranteed to be present in an OS that's based on that device family, and therefore on every device running that OS.

The decision about which device family (or families) your app will *target* is yours to make. And that decision impacts your app in these important ways. It determines

- the families of devices that your app is offered to for installing from the Microsoft Store (and consequently the form factors that you need to consider when you design your app's UI), and
- the particular set of APIs that you can rely on being present on a device running your app (the host device).

By *rely on being present*, we mean that you can call those APIs without first needing to test to see whether they're present on the host device. The device family that you target provides that guarantee (different guarantees for different device families).

### Configure your target device family

In your app package manifest source file (the `Package.appxmanifest` file), the **TargetDeviceFamily** element has a **Name** attribute. The value of that attribute is the name of the device family that your app targets. The following values are valid.

- Windows.Desktop
- Windows.Holographic
- Windows.IoT
- Windows.Mobile
- Windows.Team
- Windows.Universal
- Windows.Xbox

By default, your UWP app targets the Universal device family (that is, Microsoft Visual Studio specifies `Windows.Universal` for **TargetDeviceFamily**). And that means that your app can be installed on *all* Windows 10 devices, and that you can rely on a large core set of APIs being present on the host device. An app like that needs to have a highly adaptive UI, and comprehensive input capabilities, because it can run on a wide variety of devices. See [Preview your UI on different screen sizes](#preview-your-ui-on-different-screen-sizes) later in this topic.

If you want to limit the families of devices that your app is offered to for installing from the Microsoft Store, then you can choose to target a different device family&mdash;for example, the Desktop device family (`Windows.Desktop`), or the IoT device family (`Windows.IoT`). Of course, there'll be fewer devices that can host your app, but you'll be able to rely on a larger set of APIs being present on those devices (that will be the set in the Universal device family, plus the set in the target device family). An app like that typically needs to be only moderately adaptive; it can be somewhat specialized in its UI and input capabilities, because it can run on only a specific kind of device.

> [!TIP]
> But you can also have the best of both worlds. You can configure your app to run on all Windows 10 devices, and also access the specialized capabilities of certain families of devices when you find that you're running on one. This best-of-both-worlds scenario does require a little extra work, and we'll go into the specifics of that later in this topic.

### Configure your target device family version

APIs are added to Windows over time, so another dimension to choosing a device family is deciding which version (or versions) to target. Some project types in Visual Studio have a property page in which you can configure your target platform versions. But for all project types you can configure your target platform versions right in the project file.

Here's an example showing the relevant properties in a project file.

```xml
<!-- MyProject.Xxxproj -->
<PropertyGroup Label="Globals">
    ...
    <WindowsTargetPlatformVersion>10.0.19041.0</WindowsTargetPlatformVersion>
    <WindowsTargetPlatformMinVersion>10.0.17134.0</WindowsTargetPlatformMinVersion>
    ...
</PropertyGroup>
```

At build time, these values (together with the value of **TargetDeviceFamily@Name** from `Package.appxmanifest`) are copied into the `AppxManifest.xml` file that's generated in your project's output folder. Here's an example.

```xml
<!-- AppxManifest.xml -->
<Dependencies>
    <TargetDeviceFamily Name="Windows.Universal"
        MaxVersionTested="10.0.19041.0"
        MinVersion="10.0.17134.0" />
    ...
</Dependencies>
```

**MaxVersionTested** specifies the maximum version of the device family that your app is targeting that you have tested it against. And **MinVersion** specifies the minimum version of the device family that your app is targeting. For more details, see [**TargetDeviceFamily**](../schemas/appxpackage/uapmanifestschema/element-targetdevicefamily.md).

> [!IMPORTANT]
> You should configure these version numbers by means of either your Visual Studio project's property pages, or the values of **WindowsTargetPlatformVersion** and **WindowsTargetPlatformMinVersion** in your project file. Don't edit `AppxManifest.xml`, because the build overwrites that file. And don't edit the **MinVersion** and **MaxVersionTested** attributes of the **TargetDeviceFamily** element in your app package manifest source file (the `Package.appxmanifest` file), because those values are ignored.

## Extension SDKs, and how to reference them

If in your Visual Studio project you change your target from the Universal device family to some other device family, then you need to add a reference to the extension SDK corresponding to that device family. That makes the APIs in that device family available to your project.

If, for example, you target the IoT device family, then (with the project node selected in Solution Explorer) click **Project** > **Add Reference...** > **Universal Windows** > **Extensions**, and select the appropriate version of **Windows IoT Extensions for the UWP**. For example, if the newest IoT API that you want to call was introduced in version 10.0.17134.0, then select that version.

![Select the IoT extension SDK](images/SelectIoTExtensionSDK.png)

And this is how that reference would look in your project file.

```xml
<ItemGroup>
    <SDKReference Include="WindowsIoT, Version=10.0.17134.0" />
</ItemGroup>
```

The name and version number match the folders in the installed location of your SDK. For example, the above information matches the folder named

`\Program Files (x86)\Windows Kits\10\Extension SDKs\WindowsIoT\10.0.17134.0` 

Other extension SDKs include **Windows Desktop Extensions for the UWP**, **Windows Mobile Extensions for the UWP**, and **Windows Team Extensions for the UWP**.

If you leave your app targeting the Universal device family, then you can still add a reference to one or more extension SDKs. Reference whichever extension SDKs contain the additional APIs that you'd like to call. Remember, you're targeting the Universal device family, so those are the only APIs that you can *rely on*  being present. For APIs in the extension SDK(s) you referenced, you'll need to test that they're present on the host device at run time before you call them (more details in the [Writing code](#writing-code) section later in this topic). Of course, you don't need to perform that test for APIs in the Universal device family. This is the best-of-both-worlds scenario that we mentioned in the previous section.

By using an extension SDK, you can target the unique APIs of a specific family of devices, and thereby access their specialized capabilities. You can do that whether you target the corresponding device family or not.

## API contracts, and how to look them up

The APIs in a device family are subdivided into groups known as API contracts. When a new version of a device family is released, that new version essentially just represents the collection of new versions of all of the API contracts that belong to that device family.

For example, the API contract named `Windows.Foundation.UniversalApiContract` was at version 6.0 when it shipped with version 10.0.17134.0 of the Universal device family. But that same contract was at version 10.0 when it shipped with version 10.0.19041.0 of that same device family.

### Look up the API contract for a WinRT API

Let's see how you can look up the API contract name and version number for any given Windows Runtime API. In the [Writing code](#writing-code) section later in this topic, you'll see why and how you might use that information.

As our first example, we'll take the [**StorageFolder.TryGetChangeTracker**](/uwp/api/windows.storage.storagefolder.trygetchangetracker) method. In the **Windows 10 requirements** section of that topic, we can see that **StorageFolder.TryGetChangeTracker** was first introduced with version 6.0 of `Windows.Foundation.UniversalApiContract`.

Next, let's look at the topic for the [**StorageFolder.TryGetItemAsync**](/uwp/api/windows.storage.storagefolder.trygetitemasync) method. There is no **Windows 10 requirements** section in that topic. Instead, look at the topic for the [**StorageFolder**](/uwp/api/windows.storage.storagefolder) class itself. The **Windows 10 requirements** section there has the answer. Because the **StorageFolder.TryGetItemAsync** topic doesn't say any different, we can conclude that it shares its requirements with its parent class. So **StorageFolder.TryGetItemAsync** was first introduced with version 1.0 of `Windows.Foundation.UniversalApiContract`.

## How to choose a device family to target

Here are some considerations to help you decide which device family to target. For more details, see [**TargetDeviceFamily**](../schemas/appxpackage/uapmanifestschema/element-targetdevicefamily.md).

### Maximize your app's reach

To reach the maximum range of kinds of devices with your app, and consequently to have it run on as many devices as possible, your app should target the Universal device family. Specifically, as we've seen, you'll target a range of versions of the Universal device family.

### Limit your app to one kind of device

You may not want your app to run on a wide range of device form factors; perhaps it's specialized for a desktop PC, or for an Xbox console. In that case, you can choose to target one of the child device families.

### Limit your app to a subset of all possible devices

Instead of targeting the Universal device family, or targeting one of the child device families, you can instead target two (or more) child device families. Targeting Desktop and Mobile might make sense for your app. Or Desktop and Team. Or Desktop, Mobile, and Team, and so on.

### Exclude support for a particular version of a device family

In rare cases, you might want your app to run everywhere *except* on devices with a particular version of a particular device family. For example, let's say that your app targets version 10.0.x.0 of the universal device family. When the operating system version changes in the future&mdash;say to 10.0.x.2&mdash;at that point, you can specify that your app runs everywhere except version 10.0.x.1 of Xbox by targeting your app to 10.0.x.0 of Universal and 10.0.x.2 of Xbox. Your app will then be unavailable to the set of device family versions within Xbox 10.0.x.1 (inclusive) and earlier.

## Writing code

Much of your code will be universal in the sense that it will run the same way on every device. But for code tailored to a particular device family, you'll have the option to use adaptive code. Let's consider these different cases.

### Call an API that's implemented by your target device family

Whenever you want to call an API in a UWP app, you'll want to know whether or not the API is implemented by the device family that your app is targeting. Visual Studio IntelliSense shows you the APIs in the Universal device family *plus* the APIs that are available for any extension SDK(s) that you've referenced.

The Windows Runtime API reference documentation tells you which device family an API is part of. If you look up the API reference topic for a Windows Runtime API and look for the **Windows 10 requirements** section, then you'll see what the implementing device family is, and which version of that device family the API first appears in. If there is no **Windows 10 requirements** section, then look at the member's owning class, and see the info in the **Windows 10 requirements** section there. That info will apply to the member also.

### Call an API that's not implemented by your target device family

There'll be cases when you want to call an API in an extension SDK that you've referenced, but that API is not part of the device family that you're targeting.

For example, you might be targeting the Universal device family, but there's a desktop API that you'd like to call whenever your app is running on a desktop device.

Or your app might support early versions of a device family, but there's an API that you want to call that's available only in very recent versions of the same device family.

In cases like those, you can opt to write adaptive code so that you can call those APIs safely. The next section shows you how.

### Write adaptive code by using **ApiInformation**

There are two steps involved in using adaptive code to call an API conditionally. The first step is to make the API available to your project. To do that, add a reference to the extension SDK that represents the device family that owns the API.

The second step is to use the [**ApiInformation**](/uwp/api/windows.foundation.metadata.apiinformation) class in a condition in your code to test for the presence of the API that you want to call. This condition is evaluated wherever and whenever your app runs. But it evaluates to `true` only on devices where the API is present and therefore available to call.

If you want to call just a small number of APIs, then you can use the [**ApiInformation.IsTypePresent**](/uwp/api/Windows.Foundation.Metadata.ApiInformation) method like this.

```csharp
// Cache the value, instead of querying it multiple times.
bool isHardwareButtonsAPIPresent =
    Windows.Foundation.Metadata.ApiInformation.IsTypePresent("Windows.Phone.UI.Input.HardwareButtons");

if (isHardwareButtonsAPIPresent)
{
    Windows.Phone.UI.Input.HardwareButtons.CameraPressed += HardwareButtons_CameraPressed;
}
```

In this case, there's confidence that the presence of the [**HardwareButtons**](/uwp/api/Windows.Phone.UI.Input.HardwareButtons) class implies the presence of the [**CameraPressed**](/uwp/api/Windows.Phone.UI.Input.HardwareButtons) event, because the class and the member have the same requirements info. But in time, new members will be added to already-introduced classes, and those members will have later *introduced in* version numbers. In such cases, instead of using **IsTypePresent**, you can test for the presence of individual members by using **IsEventPresent**, **IsMethodPresent**, **IsPropertyPresent**, and similar methods. Here's an example.

```csharp
bool isHardwareButtons_CameraPressedAPIPresent =
    Windows.Foundation.Metadata.ApiInformation.IsEventPresent
        ("Windows.Phone.UI.Input.HardwareButtons", "CameraPressed");
```

As we know, the set of APIs within a device family is further broken down into subdivisions known as API contracts. You can use the **ApiInformation.IsApiContractPresent** method to test for the presence of an API contract. This is an efficient way of executing a single condition in order to know about the presence or otherwise of a large number of APIs that all belong to the same version of an API contract.

For info about how to determine the API contract that first introduced the API(s) of interest, see the [Look up the API contract for a WinRT API](#look-up-the-api-contract-for-a-winrt-api) section earlier in this topic.

Once you have that info, you can plug it into your adaptive code. For example, if the API contract's name is `Windows.Devices.Scanners.ScannerDeviceContract`, and its major and minor version numbers are 1 and 0, respectively, then your condition will look like the example below.

```csharp
bool isWindows_Devices_Scanners_ScannerDeviceContract_1_0Present =
    Windows.Foundation.Metadata.ApiInformation.IsApiContractPresent
        ("Windows.Devices.Scanners.ScannerDeviceContract", 1, 0);
```

## Preview your UI on different screen sizes

We recommend that you maximize the reach of your app. But even if you target only one kind of device form factor, there'll still likely be different sizes of screen that your app could end up being displayed on.

When you're ready to see how your app looks and lays out on a particular size of screen, use the device preview toolbar in Visual Studio to preview your UI on a small or medium mobile device, on a PC, or on a large TV screen. That way, if you've used XAML's adaptive layout features (see [Tutorial: Create adaptive layouts](/windows/uwp/design/basics/xaml-basics-adaptive-layout)), then you can test that, too.

![visual studio 2015 device preview toolbar](images/vs2015-device-preview-toolbar.png)

You don't have to make a decision in advance about every device type that you'll support. You can add an additional device size to your project at any time.

## See also

* [Device family extension SDKs and API contracts](./index.md)
* [TargetDeviceFamily](../schemas/appxpackage/uapmanifestschema/element-targetdevicefamily.md)
* [Tutorial: Create adaptive layouts](/windows/uwp/design/basics/xaml-basics-adaptive-layout)
* [What's a Universal Windows Platform (UWP) app](/windows/uwp/get-started/universal-application-platform-guide)
* [Version-adaptive apps](/windows/uwp/debug-test-perf/version-adaptive-apps)
