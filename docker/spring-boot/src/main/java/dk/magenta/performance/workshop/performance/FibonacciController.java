package dk.magenta.performance.workshop.performance;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FibonacciController {

    @RequestMapping("/fib")
    public FibResponse greeting(@RequestParam(value="n", defaultValue="10") int n) {
        return new FibResponse(Integer.toString(fib(n)));
    }

    private int fib(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fib(n - 2) + fib(n - 1);
        }
    }
}