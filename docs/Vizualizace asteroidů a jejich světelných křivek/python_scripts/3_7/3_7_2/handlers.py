        @self.canvas.events.key_press.connect
        def on_key_press(event):

            if event.key in ['q', 'Q']:
                vispy.app.quit()

            elif event.key == '1':
                plot_fluxes(phi=self.phi_i)
                wireframe_filter.enabled = False
            ...

        self.canvas.show()