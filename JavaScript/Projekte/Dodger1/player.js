class Player {
  constructor(img, xx, yy) {
    this.image = img;
    this.width = xx;
    this.height = yy;
    this.x = 0; this.xDiff = 0;
    this.y = 0; this.yDiff = 0;
    this.ms = 0;
  }
  // Position und Geschwindigkeit
  setPosition(x, y) {
    this.x = x; this.y = y;
  }
  setSpeed(dx, dy, ms) {
    this.xDiff = dx;
    this.yDiff = dy;
    this.ms = ms;
  }
  changePosition() {
    this.x += this.xDiff;
    this.y += this.yDiff;
  }
  // Grenzkontrollen
  controlBorder(xL, xR, yT, yB) {
    if (this.x < xL || this.x > xR) this.xDiff = -this.xDiff;
    if (this.y < yT || this.y > yB) this.yDiff = -this.yDiff;
  }
  controlEdge(xL, xR, yT, yB) {
    if (this.x < xL) this.x = xR;
    if (this.y < yT) this.y = yB;
    if (this.x > xR) this.x = xL;
    if (this.y > yB) this.y = yT;
  }
  controlXEdge(xL, xR, yT, yB) {
    var edge = false;
    if (this.x < xL) { this.x = xR; edge = true; }
    if (this.y < yT) { this.y = yB; edge = true; }
    if (this.x > xR) { this.x = xL; edge = true; }
    if (this.y > yB) { this.y = yT; edge = true; }
    return edge;
  }

  // Darstellung
  showImage() {
    context.drawImage(this.image, this.x, this.y, this.width, this.height); 
  }
}
  