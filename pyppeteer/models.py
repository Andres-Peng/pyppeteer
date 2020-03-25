"""Type definitions for widely used types"""
import os
from pathlib import Path

try:
    from typing import TypedDict, Sequence, Union, Literal, Dict, List, Any, TYPE_CHECKING
except ImportError:
    from typing import TypedDict

if TYPE_CHECKING:
    from pyppeteer.jshandle import JSHandle


class Viewport(TypedDict, total=False):
    width: float
    height: float
    deviceScaleFactor: float
    isMobile: bool
    isLandscape: bool
    hasTouch: bool


class BrowserOptions(TypedDict, total=False):
    ignoreHTTPSErrors: bool
    defaultViewport: Viewport
    slowMo: float


class ChromeArgOptions(TypedDict, total=False):
    headless: bool
    args: Sequence[str]
    userDataDir: str
    devtools: bool


class LaunchOptions(TypedDict, total=False):
    executablePath: str
    ignoreDefaultArgs: Union[Literal[False], Sequence[str]]
    handleSIGINT: bool
    handleSIGTERM: bool
    handleSIGHUP: bool
    timeout: float
    dumpio: bool
    env: Dict[str, Union[str, bool]]


class DeviceDetails(TypedDict):
    userAgent: str
    viewport: Viewport


class ScreenshotClip(TypedDict, total=False):
    x: float
    y: float
    width: float
    height: float
    scale: float


class CoverageResult(TypedDict):
    url: str
    ranges: Any
    text: str


JSFunctionArg = Union['JSHandle', str, int, float, bool, None, Dict[str, Any], List[Any]]
Devices = Dict[str, DeviceDetails]
platforms = ('linux', 'mac', 'win32', 'win64')
Platforms = Literal[platforms]
MouseButton = Literal['left', 'right', 'middle']
WaitTarget = Literal['load', 'domcontentloaded', 'networkidle0', 'networkidle2']
WaitTargets = Union[WaitTarget, Sequence[WaitTarget]]


class RevisionInfo(TypedDict):
    folderPath: Union[Path, os.PathLike]
    executablePath: Union[Path, os.PathLike]
    url: str
    local: bool
    revision: str