#include <windows.h>

HHOOK hHook = NULL;

LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT *pKeyboard = (KBDLLHOOKSTRUCT *)lParam;
        // Check if the pressed key is a function key
        if (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN) {
            switch (pKeyboard->vkCode) {
                case VK_F1:
                case VK_F2:
                case VK_F3:
                case VK_F4:
                case VK_F5:
                case VK_F6:
                case VK_F7:
                case VK_F8:
                case VK_F9:
                case VK_F10:
                case VK_F11:
                case VK_F12:
                    return 1; // Block default behavior
            }
        }
    }
    return CallNextHookEx(hHook, nCode, wParam, lParam);
}

int main() {
    HINSTANCE hInstance = GetModuleHandle(NULL);
    hHook = SetWindowsHookEx(WH_KEYBOARD_LL, LowLevelKeyboardProc, hInstance, 0);

    if (!hHook) {
        MessageBox(NULL, "Failed to install hook!", "Error", MB_ICONERROR);
        return 1;
    }

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(hHook);
    return 0;
}
