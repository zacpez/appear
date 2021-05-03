describe('Appear frontend renders', () => {
  test('open app correctly', (browser) => {
    const main = browser.page.main()
    main.navigate()
    main.assert.visible('@appearTitle')
    main.assert.visible('@footer')
    browser.end()
  })
})
