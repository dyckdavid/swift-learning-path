# Widget Extension (create in Xcode)

This folder is a placeholder. On your Mac:

1. Open `WidgetsLiveActivities.xcodeproj`
2. File → New → Target → **Widget Extension**
3. Enable **Include Live Activity** if the template offers it
4. Move shared `FocusAttributes` into a shared framework or shared folder membership (app + extension)

Info.plist keys to confirm:
- `NSSupportsLiveActivities` = YES (app)
- Relevant App Group if sharing data with UserDefaults/files
